from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import joblib
import string
import re


app = FastAPI()

model = joblib.load(r"C:\Users\shabb\Desktop\Fake_News_detector\model\Fake_news_model.pkl")


class NewsItem(BaseModel):
    text: str

def clean_text(text):
    text = text.lower()
    text = re.sub('\n',"",text) 
    text = re.sub(r"http\S+", "", text)  
    text = re.sub(r"\d+", "", text)  
    text = text.translate(str.maketrans('', '', string.punctuation))  
    text = re.sub(r"\s+", " ", text)  
    return text.strip()

@app.post('/predict')
def predict(news: NewsItem):
    cleaned_text = clean_text(news.text)
    prediction = model.predict([cleaned_text])[0]
    if prediction==1:
        Label="Real"
    else:
        Label="Fake"
    return {"Prediction":Label}