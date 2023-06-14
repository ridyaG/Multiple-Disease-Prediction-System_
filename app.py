import streamlit as st
import numpy as np
import pickle

# Load the trained models
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
parkinson_model = pickle.load(open('parkinson_model.sav', 'rb'))
heart_disease_model = pickle.load(open('heart_disease_model.pkl', 'rb'))

st.set_page_config(page_title='Disease Prediction App', page_icon=':hospital:')

# Define the function for diabetes prediction
def diabetes_prediction(input_data):
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    prediction = diabetes_model.predict(input_data_reshaped)
    if prediction[0] == 0:
        return 'The person is not diabetic'
    else:
        return 'The person is diabetic'

# Define the function for Parkinson's disease prediction
def parkinson_prediction(input_data):
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    prediction = parkinson_model.predict(input_data_reshaped)
    if prediction[0] == 0:
        return "The Person does not have Parkinson's Disease"
    else:
        return "The Person has Parkinson's Disease"

# Define the function for heart disease prediction
def heart_disease_prediction(input_data):
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    prediction = heart_disease_model.predict(input_data_reshaped)
    if prediction[0] == 0:
        return 'No Heart Disease Detected for the Person'
    else:
        return 'Heart Disease Detected for the Person!! Consult Doctor Immediately'

# Define the Streamlit app
def main():
    st.title('Multiple Disease Prediction System')


    # Create a sidebar for disease selection
    selected_disease = st.sidebar.selectbox('Select Disease', ('Diabetes', "Parkinson's Disease", 'Heart Disease'))

    if selected_disease == 'Diabetes':
        # Display input fields for diabetes prediction
        st.subheader('Diabetes Prediction')
        image = 'diabetes.png'  # Replace with the path to your image
        st.image(image, width=500)
        pregnancies = st.number_input('Number of Pregnancies', min_value=0, step=1, value=0)
        glucose = st.number_input('Amount of Blood Glucose Level', min_value=0.0, step=1.0, value=0.0)
        blood_pressure = st.number_input('Blood Pressure Value', min_value=0.0, step=1.0, value=0.0)
        skin_thickness = st.number_input('Skin Thickness Value', min_value=0.0, step=1.0, value=0.0)
        insulin = st.number_input('Insulin Level', min_value=0.0, step=1.0, value=0.0)
        bmi = st.number_input('Body Mass Index Value', min_value=0.0, step=1.0, value=0.0)
        diabetes_pedigree = st.number_input('Diabetes Pedigree Function Value', min_value=0.0, step=0.01, value=0.0)
        age = st.number_input('Age of the person', min_value=0, step=1, value=0)

        # When the user clicks the 'Predict' button, make the diabetes prediction
        if st.button('Predict'):
            input_data = [pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age]
            prediction = diabetes_prediction(input_data)
            st.write(prediction)

    elif selected_disease == "Parkinson's Disease":
        # Display input fields for Parkinson's disease prediction
        st.subheader("Parkinson's Disease Prediction")
        image = 'parkinson.jpg'  # Replace with the path to your image
        st.image(image,width=500)
        st.write(" ")
        st.write(
            "<h3>Enter some biomedical voice measurements to predict whether or not a person has Parkinson's Disease.</h3>",
            unsafe_allow_html=True)

        st.write(" ")

        fo = st.number_input("Average vocal fundamental frequency(Hz):", value=0.00)
        fhi = st.number_input("Maximum vocal fundamental frequency(Hz):", value=0.00)
        flo = st.number_input("Minimum vocal fundamental frequency:", value=0.000)

        st.write(" ")

        st.write("<h4>Enter some measures of variation in fundamental frequency</h4>", unsafe_allow_html=True)

        st.write(" ")

        jitter_percent = st.number_input("Multi-Dimensional Voice Program Jitter(%):", value=0.0000)
        jitter_abs = st.number_input("Multi-Dimensional Voice Program Jitter(Abs):", value=0.0000)
        rap = st.number_input("Multi-Dimensional Voice Program Relative Amplitude Perturbation:", value=0.0000)
        ppq = st.number_input("Multi-Dimensional Voice Program five-point Period Perturbation Quotient:", value=0.0000)
        jitter_ddp = st.number_input("Average absolute difference of differences between jitter cycles:", value=0.0000)

        st.write(" ")

        st.write("<h4>Enter some measures of variation in amplitude</h4>", unsafe_allow_html=True)

        st.write(" ")

        shimmer = st.number_input("Multi-Dimensional Voice Program Shimmer:", value=0.0000)
        shimmer_db = st.number_input("Multi-Dimensional Voice Program Shimmer(dB):", value=0.000)
        apq3 = st.number_input("Three-point Amplitude Perturbation Quotient:", value=0.0000)
        apq5 = st.number_input("Five-point Amplitude Perturbation Quotient:", value=0.0000)
        apq = st.number_input("Amount of Aphomorphine: ", value=0.0000)
        dda = st.number_input("MDVP 11-point Amplitude Perturbation Quotient:", value=0.0000)

        st.write(" ")

        st.write("<h4>Enter the measures of ratio of noise to tonal components in the voice</h4>",
                 unsafe_allow_html=True)

        st.write(" ")

        nhr = st.number_input("Noise-to-harmonics ratio:", value=0.0000)
        hnr = st.number_input("Harmonics-to-noise ratio:", value=0.000)

        st.write(" ")

        st.write("<h4>Enter the nonlinear dynamical complexity measures</h4>", unsafe_allow_html=True)

        st.write(" ")

        rpde = st.number_input("Recurrence Period Density Entropy measure:", value=0.0000)
        d2 = st.number_input("Correlation Dimension:", value=0.0000)

        st.write(" ")

        dfa = st.number_input("Signal fractal scaling exponent of Detrended Fluctuation Analysis:", value=0.0000)

        st.write(" ")

        st.write("<h4>Enter the nonlinear measures of fundamental frequency variation</h4>", unsafe_allow_html=True)

        st.write(" ")

        spread1 = st.number_input("Two nonlinear measures of fundamental:", value=0.0000)
        spread2 = st.number_input("Frequency variation:", value=0.0000)
        ppe = st.number_input("Pitch Period Entropy:", value=0.0000)

        # When the user clicks the 'Predict' button, make the Parkinson's disease prediction
        if st.button('Predict'):
            input_data = [fo, fhi, flo, jitter_percent, jitter_abs, rap, ppq, jitter_ddp, shimmer, shimmer_db, apq3, apq5, apq,dda, nhr, hnr,
         rpde, dfa, spread1, spread2, d2, ppe]  # Add the input data specific to Parkinson's disease prediction
            prediction = parkinson_prediction(input_data)
            st.write(prediction)

    elif selected_disease == 'Heart Disease':
        # Display input fields for heart disease prediction
        st.subheader('Heart Disease Prediction')
        image = 'heart1.jpg'  # Replace with the path to your image
        st.image(image, width=500)
        st.write('Please input the following parameters to predict the presence of heart disease:')

        # Create sliders and dropdowns for user input
        age = st.slider('Age', 20, 100, 50)
        sex = st.selectbox('Sex', [0, 1])
        cp = st.selectbox('Chest Pain Type', [0, 1, 2, 3])
        trestbps = st.slider('Resting Blood Pressure (mm Hg)', 80, 200, 120)
        chol = st.slider('Cholesterol (mg/dL)', 100, 600, 200)
        fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dL', [0, 1])
        restecg = st.selectbox('Resting Electrocardiographic Results', [0, 1, 2])
        thalach = st.slider('Maximum Heart Rate Achieved', 70, 220, 150)
        exang = st.selectbox('Exercise Induced Angina', [0, 1])
        oldpeak = st.slider('ST Depression Induced by Exercise Relative to Rest', 0.0, 6.0, 3.0, 0.1)
        slope = st.selectbox('Slope of the Peak Exercise ST Segment', [0, 1, 2])
        ca = st.selectbox('Number of Major Vessels Colored by Flourosopy', [0, 1, 2, 3])
        thal = st.selectbox('Thalassemia', [0, 1, 2, 3])

        # When the user clicks the 'Predict' button, make the heart disease prediction
        if st.button('Predict'):
            input_data = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca,
                                       thal]  # Add the input data specific to heart disease prediction
            prediction = heart_disease_prediction(input_data)
            st.write(prediction)

# Run the Streamlit app
if __name__ == '__main__':
    main()

