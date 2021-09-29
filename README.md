# 😷 **Face mask detection** 😷
Experiment face mask detection with YOLOv5 models <a href="https://wandb.ai/lannguyen/face-mask-yolov5"><img src="https://raw.githubusercontent.com/wandb/assets/main/wandb-github-badge-gradient.svg" alt="WandB"></a>

## 🌟 **Run on Google Colab (Recommend)**
- Open notebook and follow the instructions [![Notebook](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1KTAk_kdO74OvXMGxdGdOLx6QPu3Yr0rb?usp=sharing)

## 🌟 **Run on local machine (Require CUDA)**
- Clone the repo
```
git clone https://github.com/lannguyen0910/face-mask-yolov5/
cd face-mask-yolov5/deployment/
```
- Install dependencies
```
pip install -r requirements.txt
```
- Download yolov5 weights (About 1.3Gb)
```
- python download_weights.py
```
- Start the app. Options: [yolov5s.pt | yolov5m.pt | yolov5l.pt | yolov5x.pt]
```
python app.py --host=localhost:3000 --weights './model/weights/yolov5s.pt'
```

🚨 There is a high chance that you'll face some errors when run the app on local machine. Feel free to make a pull request!  

## 🌟 **Train YOLOv5 models** 
- Open notebook and follow the instructions [![Notebook](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1ZUZHRlUe6wgXHjdjbHf7-npJAhSPJUwn?usp=sharing)

## 🌟 **Results**
<p align="center">
    <img src="./assets/results/face-mask.jpg" style="width:50%" />
    <img src="./assets/results/face-not-mask.jpg" style="width:50%" />
</p>

## 🌟 **Experiments**
**Full experiment details on** <a href="https://wandb.ai/lannguyen/face-mask-yolov5"><img src="https://raw.githubusercontent.com/wandb/assets/main/wandb-github-badge-gradient.svg" alt="WandB"></a>
<br>

### **Metrics**
<p align="center">
    <img src="./assets/experiments/metrics_all.PNG" style="width:50%" />
    <img src="./assets/experiments/mAP_0.5.PNG" style="width:50%" />
    <img src="./assets/experiments/mAP_0.5_0.95.PNG" style="width:50%" />
</p>

### **Lossses**

<p align="center">
    <img src="./assets/experiments/train_loss.PNG" style="width:50%" />
    <img src="./assets/experiments/val_loss.PNG" style="width:50%" />
</p>

# 📙 **References**
- https://github.com/waittim/mask-detector