import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    str_user_input = [str(x) for x in request.form.values()]
    
    #Retriving User contat details only
    retrive_contact_values_str=str_user_input[0:3]
    #Retriving Name
    retrive_Name=retrive_contact_values_str[0]
    #Retriving Contact
    retrive_Contact=retrive_contact_values_str[1]
    #Retriving Email
    retrive_Email=retrive_contact_values_str[2]
    
    #Retriving model values only
    retrive_model_values_str=str_user_input[3:]
    #Converting model str values into int values
    for i in range(0, len(retrive_model_values_str)):
        retrive_model_values_str[i]=int(retrive_model_values_str[i])
        
    #Retriving experience
    retrive_experience=retrive_model_values_str[0]
    #Retriving test_score
    retrive_test_score=retrive_model_values_str[1]
    #Retriving interview_score
    retrive_interview_score=retrive_model_values_str[2]
    
    # Putting the int values of model into the array
    retrive_model_values_int_array = [np.array(retrive_model_values_str)]
    
    #Comparing the values of user input model values with the dataset(ML)
    prediction = model.predict(retrive_model_values_int_array)
    # Storing the result of ML operation after comparing
    output = round(prediction[0], 2)
    
    #Return all values to the output.html page
    return render_template('output.html', your_name='{}'.format(retrive_Name), your_contact='{}'.format(retrive_Contact), your_email='{}'.format(retrive_Email), your_experience='{}'.format(retrive_experience), your_test_score='{}'.format(retrive_test_score), your_interview_score='{}'.format(retrive_interview_score), prediction_sallary='{}'.format(output))

if __name__ == "__main__":
    app.run()
