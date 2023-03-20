# CountButterfly

This task is based on yolov5 to produce butterfly detection<br>
See the [YOLOv5](https://github.com/ultralytics/yolov5) for the reference

Install

a. Install [conda](https://docs.conda.io/en/latest/) and create virtual environment for this task
```bash
conda create -n countbutterfly python=3.7
conda activate countbutterfly
conda install pip
```
b. Clone yolov5 repo and install [requirements.txt](https://github.com/ultralytics/yolov5/blob/master/requirements.txt) in a
[**Python>=3.7.0**](https://www.python.org/) environment, including
[**PyTorch>=1.7**](https://pytorch.org/get-started/locally/).

```bash
git clone https://github.com/ultralytics/yolov5  # clone
cd yolov5
pip install -r requirements.txt  # install
```
c. Clone this repo and put all the files into yolov5 folder. 
```bash
git clone https://github.com/hhlim333/CountButterfly.git
```
d. Put butterfly.yaml into "data/" folder and (train,valid) folder into "data/image/" folder


</details>

# 1. Training Custom dataset (butterfly) for yolov5 model.
a. You can use your computer<br>
```bash
cd yolov5
python train.py --img 250 --batch 14 --epochs 150 --data data/butterfly.yaml --weights yolov5s.pt --nosave --cache
```
b. google-colab<br>
https://colab.research.google.com/drive/1LSNiUjIzOLYqoQ929K0qCcglM9ulgdK4?usp=sharing

After training, you can get the last.pt file for the trained model

# 2. Using trained model to produce butterfly detection for the youtube video.
Using counterbutterfly.py to show the result.
```bash
python countbutterfly.py
```
