import streamlit as st
import pickle

# Load the trained logistic regression model
model = pickle.load(open('titanic_logreg_model.pkl', 'rb'))

# Set the title for the web app
st.title('Titanic Survival Prediction')

# Create sliders and selection boxes for user input
age = st.slider('Age', 1, 100, 25)  # Default value is 25
fare = st.slider('Fare', 0, 500, 50)  # Default value is 50
pclass = st.selectbox('Passenger Class (Pclass)', [1, 2, 3])
sex = st.selectbox('Sex', ['Male', 'Female'])

# Convert categorical variable 'Sex' to numeric (1 for Male, 0 for Female)
sex = 1 if sex == 'Male' else 0

# Predict survival based on user input
if st.button('Predict'):
    # Make a prediction based on user inputs
    prediction = model.predict([[pclass, age, fare, sex]])
    
    # Display the result
    if prediction == 1:
        st.success('The passenger would have survived.')
    else:
        st.error('The passenger would not have survived.')
