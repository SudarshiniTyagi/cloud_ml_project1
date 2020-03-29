This is the bare metal code directory. 

This code contains the following two files:
1. run_k80.s - use this file to run on GPU k80
2. run_p40.s - use this file to run on GPU p40

Steps:
1. `git clone <this repo>`
2. Open file `run_k80.s` and replace `~/pytorch_env/py3.6.3/bin/python` with the python you are using. 
    Steps to create virtual env are:
    ```
    Python environment Virtualenv setup (first time)
      • mkdir pytorch_env; cd pytorch_env
      • virtualenv - - system-site-packages py3.6.3
      • source py3.6.3/bin/activate
      • pip3 install http://download.pytorch.org/whl/cu92/torch-0.4.1-cp36-cp36m-linux_x86_64.whl
      • pip3 install torchvision
      • source ~/pytorch_env/py3.6.3/bin/activate
    ```
2. If running on k80, submit the batch job using `sbatch run_k80.s`
3. Similarly, if running on p40, change the python path and submit the batch job using `sbatch run_p40.s`


