import os

os.system("stylegan2_pytorch --new --data ./MLHW_6/faces/faces --batch-size 4 --num-image-tiles 4 --save-every 5000 --evaluate-every 5000 --image-size 128 --num-train-steps 80000 --network-capacity 20 --gradient-accumulate-every 1 --attn-layers [1,2] --aug-prob 0.25 --aug-types [translation,cutout,color]")


