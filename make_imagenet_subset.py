import os
import shutil

base = "/scratch/work/public/imagenet/train/"

for j, sub in enumerate(os.listdir(base)):
    class_dir = base + sub
    if not os.path.isdir("/scratch/st3688/imagenet_small_subset/train/"+sub):
        os.mkdir("/scratch/st3688/imagenet_small_subset/train/"+sub)
        os.mkdir("/scratch/st3688/imagenet_small_subset/test/"+sub)
        os.mkdir("/scratch/st3688/imagenet_small_subset/val/"+sub)
        for i, file_name in enumerate(os.listdir(class_dir)):
            f = class_dir + "/" + file_name
            if i<20:
                shutil.copy(f, "/scratch/st3688/imagenet_small_subset/train_new/" + sub + "/" + file_name)
            elif i>=20 and i<30:
                shutil.copy(f, "/scratch/st3688/imagenet_small_subset/test/" + sub + "/" + file_name)
                continue
            elif i>=30 and i<40:
                shutil.copy(f, "/scratch/st3688/imagenet_small_subset/val/" + sub + "/" + file_name)
                continue
            else:
                break
        print(j,"/1000 folders done")
