from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('titanic_model.pkl')  # Load trained model

@app.route('/', methods=['GET', 'POST'])
def predict():
    prediction = None
    if request.method == 'POST':
        # Get input values from form
        pclass = int(request.form['pclass'])
        sex = int(request.form['sex'])  # 0 = female, 1 = male
        age = float(request.form['age'])
        fare = float(request.form['fare'])

        # Make prediction
        input_features = np.array([[pclass, sex, age, fare]])
        pred = model.predict(input_features)[0]
        prediction = "Survived ✅" if pred == 1 else "Did Not Survive ❌"

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
