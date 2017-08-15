import numpy as np
import random

import utils
import synapses

class CountingSource(object):
    """
    Counting source (Lazar et. al 2009)
        This source is composed of randomly alternating sequences of size L+2
        of the form 'abb...bbc' and 'dee...eef'.
    """
    def __init__(self, words, probs, N_u_e, overlap = False):

        self.word_index = 0                      # index for word
        self.ind = 0                             # index within word
        self.glob_ind = 0                        # global index
        self.words = words                       # different words
        self.probs = probs                       # transition probabilities
        self.N_u_e = int(N_u_e)                  # active per step

        # alphabet: lookup is a dictionary with letters and indices
        self.alphabet = ''.join(sorted(''.join(set(''.join(self.words)))))
        self.N_a = len(self.alphabet)
        self.lookup = dict(zip(self.alphabet,range(self.N_a)))

        # overlap for input neuron pools
        self.overlap = overlap

    def generate_connection_e(self, N_e):
        """
        Generate the W_eu connection matrix

        Parameters:
            N_e: number of excitatory neurons
        """

        # always overlap if there is not enough neuron pools for the alphabet
        if self.N_u_e * self.N_a > N_e:
            self.overlap = True

        # choose random input neuron pools
        W = zeros((N_e,self.N_a))
        available = set(range(N_e))
        for a in range(self.N_a):
            temp = random.sample(available,self.N_u_e)
            W[temp,a] = 1
            if not self.overlap:
                available -= set(temp)

        # always use a full synaptic matrix
        ans = synapses.FullSynapticMatrix((N_e,self.N_a))

        return ans

    def char(self):
        """
        Return the current alphabet character
        """
        word = self.words[self.word_index]
        return word[self.ind]

    def sequence_ind(self):
        """
        Return current intra-word index
        """
        return self.ind

    def index(self):
        """
        Return character index
        """
        character = self.char()
        ind = self.lookup[character]
        return ind

    def next_word(self):
        """
        Start a new word, with transition probability from probs
        """
        self.ind = 0
        w = self.word_index
        p = self.probs[w,:]
        self.word_index = find(rand()<=cumsum(p))[0]

    def next(self):
        """
        Return next word character or first character of next word
        """
        self.ind += 1
        self.glob_ind += 1

        string = self.words[self.word_index]
        if self.ind >= len(string):
            self.next_word()
        ans = zeros(self.N_a)
        ans[self.index()] = 1
        return ans