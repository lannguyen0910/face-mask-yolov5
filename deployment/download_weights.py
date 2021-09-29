import gdown
import os

weight_url = {
    "yolov5s": "https://drive.google.com/uc?id=1aZeLQ9Q2dSK9eFfBM3PQpvf_I3IAz5PR",
    "yolov5m": "https://drive.google.com/uc?id=1W46Wtq5kvZcM4HiV9hG5XOB6RvBnfTni",
    "yolov5l": "https://drive.google.com/uc?id=1r8eJcwJKTrlF9AXdtGtmsJrJd_qqzGhL",
    "yolov5x": "https://drive.google.com/uc?id=11-rKfxVA0rneZT6nS0XcMIRKUPV2o43_",
}

output_path = {
    "yolov5s": "./models/weights/yolov5s.pt",
    "yolov5m": "./models/weights/yolov5m.pt",
    "yolov5l": "./models/weights/yolov5l.pt",
    "yolov5x": "./models/weights/yolov5x.pt",
}

models = ['yolov5s', 'yolov5m', 'yolov5l', 'yolov5x']

if __name__ == '__main__':
    weights_path = './models/weights'
    if not os.path.exists(weights_path):
        os.makedirs(weights_path, exist_ok=True)

    for model in models:
        gdown.download(weight_url[model], output_path[model], quiet=False)
