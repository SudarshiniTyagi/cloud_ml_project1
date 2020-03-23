#!/bin/bash

#SBATCH --job-name=cloudml_imagenet
#SBATCH --reservation=chung
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=28
#SBATCH --mem=16GB
#SBATCH --gres=gpu:p40:4
#SBATCH --time=4:00:00
#SBATCH --output=slurm_resnet18_b128_p40.out

module load  python3/intel/3.6.3 cuda/9.0.176  nccl/cuda9.0/2.4.2

~/pytorch_env/py3.6.3/bin/python examples/imagenet/main.py -a resnet18 -b 128 --lr 0.01 --epochs 1 /scratch/st3688/imagenet_small_subset/
