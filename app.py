from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load trained model
model = joblib.load('stroke_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collect input from the form
        input_data = {
            'gender': request.form['gender'],
            'age': float(request.form['age']),
            'hypertension': 1 if request.form['hypertension'] == 'Yes' else 0,
            'heart_disease': 1 if request.form['heart_disease'] == 'Yes' else 0,
            'ever_married': 1 if request.form['ever_married'] == 'Yes' else 0,
            'work_type': request.form['work_type'],
            'residence_type': 1 if request.form['residence_type'] == 'Urban' else 0,
            'avg_glucose_level': float(request.form['avg_glucose_level']),
            'bmi': float(request.form['bmi']),
            'smoking_status': request.form['smoking_status']
        }

        # Define column order expected by model
        expected_columns = ['gender', 'age', 'hypertension', 'heart_disease',
                            'ever_married', 'work_type', 'residence_type',
                            'avg_glucose_level', 'bmi', 'smoking_status']

        # Convert input to DataFrame
        input_df = pd.DataFrame([input_data])[expected_columns]

        # Make prediction
        prediction = model.predict(input_df)[0]
        result_text = "Prediction: High Risk of Stroke" if prediction == 1 else "Prediction: Low Risk of Stroke"
        result_class = "high-risk" if prediction == 1 else "low-risk"

        return render_template('index.html', prediction_text=result_text, prediction_class=result_class)

    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}", prediction_class="high-risk")

if __name__ == '__main__':
    app.run(debug=True)
