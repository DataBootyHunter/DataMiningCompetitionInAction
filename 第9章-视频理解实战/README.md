# PVU_challenge
本代码是基于mmaction2代码库的基础上开发的，mmaction2的使用教程见https://mmaction2.readthedocs.io/zh_CN/latest/index.html


## Install (cu113)

```bash
pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu113
pip install mmcv-full==1.6.0 -f https://download.openmmlab.com/mmcv/dist/cu113/torch1.11.0/index.html
pip install mmaction2
pip install timm
```
## pretrain
```bash
python tools/train.py configs/TASK/pretrain/videotext_contrast.py
```

## finetune
```bash
# VST SR 8/6
python tools/train.py configs/TASK/swin/swin8x6.py
# VST SR 24/2
python tools/train.py configs/TASK/swin/swin8x6.py
# VST SR 16/3
python tools/train.py configs/TASK/swin/swin8x6.py
# VST SR 4/12
python tools/train.py configs/TASK/swin/swin8x6.py
```

## inference
```bash
python tools/test.py $path_to_config $path_to_checkpoints --out $output_filepath
# 如
python tools/test.py configs/TASK/swin/swin8x6.py work_dirs/swin8x6/latest.pth --out output_swin8x6.json
```
集成方式使用离线集成，即使用多个模型分别使用上述指令推理，再从输出文件中读取后取均值
