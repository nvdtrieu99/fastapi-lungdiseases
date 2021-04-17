from fastapi import FastAPI, UploadFile, File
from tensorflow.python.keras.models import load_model
import numpy as np
from PIL import Image, ExifTags
import cv2


result = ["Covid19", "Binh thuong", "Benh viem phoi"]
# model = load_model('app/../model/best_model_vgg16.h5')


app = FastAPI()
@app.get('/')
async def home():
    return {
        "hello": "world"
    }

# @app.post("/uploadfile")
# async def create_upload_file(file: UploadFile = File(...)):
#     img = Image.open(file.file)
#     img = np.array(img)
#     image = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
#     image = cv2.resize(image, (128,128))
#     image = image/255.0
#     image = np.reshape(image, (1,128,128,3))
#     pre = model.predict(image)
#     chart = result[0]+":"+str(pre[0][0])+","+result[1]+":"+str(pre[0][1])+","+result[2]+":"+str(pre[0][2])
#     print(chart)
#     return [
#         {
#             "type": str(result[np.argmax(pre)]),
#             "accuracy": float("{:.4f}".format(pre[0][np.argmax(pre)])),
#             "chart": chart
#         }
#     ]

def autoRotateImage(img):
    for orientation in ExifTags.TAGS.keys():
        if ExifTags.TAGS[orientation]=='Orientation':
            break
    
    exif = img._getexif()
    if (exif!=None):
        try:
            if exif[orientation] == 3:
                img=img.rotate(180, expand=True)
            elif exif[orientation] == 6:
                img=img.rotate(270, expand=True)
            elif exif[orientation] == 8:
                img=img.rotate(90, expand=True)
        except:
            return img
    return img


@app.get("/model_accuracy")
async def getModelAccuracy():
    return float("{:.4f}".format(0.8919969201087952))
