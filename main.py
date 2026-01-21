from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load model
model = joblib.load("iris_model.pkl")

app = FastAPI(title="ML Model API with FastAPI")

class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.get("/")
def home():
    return {"message": "FastAPI ML Model running 🚀"}

@app.post("/predict")
def predict(data: IrisInput):

    input_data = np.array([[
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]])

    prediction = model.predict(input_data)[0]

    return {
        "prediction": int(prediction),
        "class_name": ["setosa", "versicolor", "virginica"][prediction]
    }
