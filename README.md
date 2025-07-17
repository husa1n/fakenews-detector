# Fake News Detection App

A machine learning web app that classifies news articles as fake or real using a RandomForest model. Built with FastAPI and Streamlit.

## Features

- Input news article text and get a prediction instantly
- Trained on a kaggle dataset
- Backend API with FastAPI
- Interactive frontend UI with Streamlit

## Technologies Used

- Python
- Scikit-learn
- FastAPI
- Streamlit
- Pandas, NumPy
- TfidfVectorizer

## How to run

- Install dependencies:
  pip install -r requirements.txt

- start the backend(FastAPI)
uvicorn main:app --reload

- start the frontend(Streamlit)
streamlit run app.py
