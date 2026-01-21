🚀 Cloud Deployment of ML App
📌 Project Overview

This project demonstrates how to deploy a Machine Learning model as a REST API on the cloud using FastAPI and GitHub, without using Docker.

The application loads a trained ML model and exposes prediction endpoints that can be accessed online.

🧠 Machine Learning Model

Algorithm: Logistic Regression

Dataset: Iris Dataset

Task: Classification

Model saved as: model.pkl

⚙️ Tech Stack

Python

FastAPI

Scikit-learn

NumPy

Uvicorn

GitHub (for version control)

Render (for cloud deployment)

📂 Project Structure
ml-api-cloud/
│
├── app.py            # FastAPI application
├── model.pkl         # Trained ML model
├── requirements.txt  # Project dependencies
└── README.md

▶️ How to Run Locally
pip install -r requirements.txt
uvicorn app:app --reload


Open in browser:

http://127.0.0.1:8000/docs

🌐 API Endpoints
Home

GET /

{
  "status": "ML API live 🚀"
}

Prediction

POST /predict

Request Body:

[5.1, 3.5, 1.4, 0.2]


Response:

{
  "prediction": 0
}

☁️ Cloud Deployment

The project is deployed directly from GitHub to the cloud using Render without Docker.

Deployment steps:

Upload project to GitHub

Connect GitHub repository to Render

Deploy as a Python Web Service

📌 Use Case

Learning ML model deployment

College project submission

Internship / fresher portfolio

👨‍💻 Author

Parv
B.Tech – Data Science / AI / ML

⭐ Acknowledgement

Iris dataset from scikit-learn library.
