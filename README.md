# Titanic Survival Prediction Web App

A Flask-based web app that predicts whether a Titanic passenger survived based on details like age, gender, class, and fare.  
The model is trained using Titanic dataset analysis (`Titanic.ipynb`) and saved as `titanic_model.pkl`.

## Features
- Input passenger details through a simple web form
- Predicts **Survived** or **Did Not Survive**
- End-to-end ML pipeline: data analysis → model training → deployment

## How to Run
```bash
git clone https://github.com/tathagat-git/Titanic-survival-prediction.git
cd Titanic-survival-prediction
pip install -r requirements.txt
python app.py
