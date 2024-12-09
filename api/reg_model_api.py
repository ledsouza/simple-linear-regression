from pydantic import BaseModel
from fastapi import FastAPI
import uvicorn
import joblib

app = FastAPI()


class RequestBody(BaseModel):
    horas_estudo: float


model = joblib.load("./../models/reg_model.pkl")


@app.post("/predict")
def predict(data: RequestBody):
    input_feature = [[data.horas_estudo]]
    y_pred = model.predict(input_feature)[0].astype(int)
    return {"pontuacao": y_pred.tolist()}
