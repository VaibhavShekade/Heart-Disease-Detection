import pickle
import streamlit as st
from streamlit_option_menu import option_menu

heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Heart Disease Detection',
                          
                          [
                            'Home',
                           'Heart Disease Detection'
                           ],
                          icons=['house','activity'],
                          default_index=0)
#home    
if (selected == 'Home'):

   st.title("Heart Disease Detection")
   st.subheader('Heart Disease Detection is system based on predictive modeling which predicts the disease of the user on the basis of the symptoms that user provides as an input to the system. ')

   st.write("##")
   st.write("##")   

   st.subheader('Team Members')
   original_title = '''<table>
        <thead>
            <tr>
            <th>Name</th>
            <th>UID</th>
            </tr>
        </thead>
        <tbody>
            <tr>
            <td>AJAY SINGH</td>
            <td>20BCS9987</td>
            </tr>
            <tr>
            <td>TEJAS SARASWAT</td>
            <td>20BCS9931</td>
            </tr>
            <tr>
            <td>PRINCE KUMAR SINGH</td>
            <td>20BCS1058</td>
            </tr>
            <tr>
            <td>SAMEER ANAND</td>
            <td>20BCS9834</td>
            </tr>
            <tr>
            <td>VAIBHAV SHEKADE</td>
            <td>20BCS1484</td>
            </tr>
        </tbody>
        </table>'''
   st.markdown(original_title, unsafe_allow_html=True)





# Heart Disease Prediction Page
if (selected == 'Heart Disease Detection'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
        
    
    

















