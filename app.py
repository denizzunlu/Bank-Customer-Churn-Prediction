import os
from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import joblib

app = Flask(__name__)

model = joblib.load("model.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        features = request.form.to_dict()
        features_df = pd.DataFrame([features])
        prediction = model.predict(features_df)[0]
        return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
