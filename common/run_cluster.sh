#!/bin/bash

#SBATCH --partition=sleuths
#SBATCH --ntasks=10
#SBATCH --mem-per-cpu=5000
#SBATCH --job-name=""
#SBATCH --output=sornA20.out
#SBATCH --mail-user=delpapa@fias.uni-frankfurt.de
#SBATCH --mail-type=END
#SBATCH --time=7-00:00:00

echo "SLURM_JOBID="$SLURM_JOBID
echo "SLURM_JOB_NODELIST"=$SLURM_JOB_NODELIST
echo "SLURM_NNODES"=$SLURM_NNODES
echo "SLURMTMPDIR="$SLURMTMPDIR

echo "working directory = "$SLURM_SUBMIT_DIR

srun python common/run_multiple.py RandomSequenceTask