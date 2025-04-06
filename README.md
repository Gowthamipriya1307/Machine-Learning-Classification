# 🧠 Stroke Prediction Using Machine Learning

This project focuses on predicting the likelihood of a stroke based on a variety of health and demographic features using machine learning. It includes thorough data preprocessing, exploratory data analysis (EDA), model training, and performance evaluation.

---

## 📄 Attribute Information

1. **id**: Unique identifier  
2. **gender**: `"Male"`, `"Female"`, or `"Other"`  
3. **age**: Age of the patient  
4. **hypertension**:  
   - `0`: No hypertension  
   - `1`: Has hypertension  
5. **heart_disease**:  
   - `0`: No heart disease  
   - `1`: Has heart disease  
6. **ever_married**: `"No"` or `"Yes"`  
7. **work_type**: `"children"`, `"Govt_job"`, `"Never_worked"`, `"Private"`, `"Self-employed"`  
8. **Residence_type**: `"Rural"` or `"Urban"`  
9. **avg_glucose_level**: Average glucose level in blood  
10. **bmi**: Body Mass Index  
11. **smoking_status**: `"formerly smoked"`, `"never smoked"`, `"smokes"`, or `"Unknown"`  
12. **stroke** (Target):  
    - `1`: Had a stroke  
    - `0`: Did not have a stroke  

---

## 🧼 Data Preprocessing

- **Missing Values**: Imputed missing values in `bmi` using the **median**, due to its right-skewed distribution.
- **Data Cleaning**: Removed the single row where gender was `"Other"`.
- **Encoding**: Applied **one-hot encoding** using `pd.get_dummies()` for categorical variables.
- **Feature Scaling**: Standardized features using **`StandardScaler()`** to normalize the data.

---

## 📈 Exploratory Data Analysis (EDA)

Visualizations were used to analyze the relationship between stroke occurrence and other features, such as:

- Gender  
- Marital status  
- Residence type  
- Work type  

Notable findings:
- Stroke cases make up only ~5% of the dataset.
- Presence of heart disease or hypertension increases the risk of stroke.
- Slight trends in marital status and work type.
---

## 🤖 Models Trained

- Logistic Regression  
- Random Forest  
- Support Vector Machine (SVM)  


### 📊 Evaluation Metrics:
- Accuracy  
- Precision  
- Recall  
- F1-score  
- ROC AUC Score

Refer to the notebook for full evaluation details and comparison charts.

---

## ✅ Results

Model performance is compared using several metrics to identify the most effective classifier for stroke prediction. Final results and interpretations are shown in the notebook.

---

## 🌐 Future Improvements

- Develop a **Flask-based web application** to make predictions via a user-friendly interface.
- Deploy the trained model as an **API** for frontend or mobile integration.
- Enhance **user experience (UX)** with visual feedback and health tips based on inputs.

---

## 🚀 Getting Started

To run this notebook locally:

```bash
git clone <https://github.com/Gowthamipriya1307/Machine-Learning-Classification>
cd Machine-Learning-Classification
jupyter notebook
