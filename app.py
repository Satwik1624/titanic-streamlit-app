# import streamlit as st
# import pickle

# # Load the trained logistic regression model
# model = pickle.load(open('titanic_logreg_model.pkl', 'rb'))

# # Set the title for the web app
# st.title('Titanic Survival Prediction')

# # Create sliders and selection boxes for user input
# age = st.slider('Age', 1, 100, 25)  # Default value is 25
# fare = st.slider('Fare', 0, 500, 50)  # Default value is 50
# pclass = st.selectbox('Passenger Class (Pclass)', [1, 2, 3])
# sex = st.selectbox('Sex', ['Male', 'Female'])

# # Convert categorical variable 'Sex' to numeric (1 for Male, 0 for Female)
# sex = 1 if sex == 'Male' else 0

# # Predict survival based on user input
# if st.button('Predict'):
#     # Make a prediction based on user inputs
#     prediction = model.predict([[pclass, age, fare, sex]])
    
#     # Display the result
#     if prediction == 1:
#         st.success('The passenger would have survived.')
#     else:
#         st.error('The passenger would not have survived.')
import streamlit as st
import pickle

# Load the saved model (update the file name here)
model = pickle.load(open('titanic_logreg_model.pkl', 'rb'))

# Title for the web app
st.title('Titanic Survival Prediction')

# Collect user inputs
pclass = st.selectbox('Passenger Class', [1, 2, 3])
age = st.slider('Age', 1, 100, 25)
fare = st.number_input('Fare', min_value=0.0, value=35.0)
sex = st.selectbox('Sex', ['Male', 'Female'])
sibsp = st.number_input('Number of Siblings/Spouses Aboard', min_value=0, value=0)
parch = st.number_input('Number of Parents/Children Aboard', min_value=0, value=0)
embarked = st.selectbox('Port of Embarkation', ['C = Cherbourg', 'Q = Queenstown', 'S = Southampton'])
ticket_class = st.selectbox('Ticket Class', [1, 2, 3])

# Encode the categorical variables
# For 'sex': 'Male' = 1, 'Female' = 0
sex_encoded = 1 if sex == 'Male' else 0

# For 'embarked': 'C' = 0, 'Q' = 1, 'S' = 2
if embarked == 'C = Cherbourg':
    embarked_encoded = 0
elif embarked == 'Q = Queenstown':
    embarked_encoded = 1
else:
    embarked_encoded = 2

# Prediction button
if st.button('Predict'):
    # Predict using all 8 features
    prediction = model.predict([[pclass, age, fare, sex_encoded, sibsp, parch, embarked_encoded, ticket_class]])

    # Display the result
    if prediction[0] == 0:
        st.error('The passenger did not survive.')
    else:
        st.success('The passenger survived.')
