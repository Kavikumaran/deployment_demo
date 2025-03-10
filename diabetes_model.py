
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models

diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

# page title
st.title('Diabetes Prediction using ML')

# getting the input data from the user
col1, col2, col3 = st.columns(3)

with col1:
    Pregnancies = st.text_input('Number of Pregnancies')

with col2:
    Glucose = st.text_input('Glucose Level')

with col3:
    BloodPressure = st.text_input('Blood Pressure value')

with col1:
    SkinThickness = st.text_input('Skin Thickness value')

with col2:
    Insulin = st.text_input('Insulin Level')

with col3:
    BMI = st.text_input('BMI value')

with col1:
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

with col2:
    Age = st.text_input('Age of the Person')

# code for Prediction
diabetic_diagnosis = ''

# creating a button for Prediction

if st.button('Diabetes Test Result'):
    diabetic_prediction = diabetes_model.predict(
        [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

    if diabetic_prediction[0] == 1:
        diabetic_diagnosis = 'The person is diabetic'
    else:
        diabetic_diagnosis = 'The person is not diabetic'

st.success(diabetic_diagnosis)