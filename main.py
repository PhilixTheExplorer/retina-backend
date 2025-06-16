from fastapi import FastAPI, File, UploadFile
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image
import io

app = FastAPI()
model = load_model("cat_dog_classifier.h5")

@app.get("/")
async def root():
    return {"message": "Hello Server! Retina backend is running successfully."}

def preprocess(img):
    img = img.resize((160, 160))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0
    return img_array

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    img = Image.open(io.BytesIO(contents)).convert('RGB')
    img_tensor = preprocess(img)
    prediction = model.predict(img_tensor)[0][0]
    label = "dog" if prediction > 0.5 else "cat"
    return {"label": label, "confidence": float(prediction)}
