from unittest import result
from flask import Flask,render_template,request
import pickle
from matplotlib.pyplot import get
import numpy as np
app=Flask(__name__)
model=pickle.load(open(r'E:\Velocity Jan2021\Daily Self study\Diabetes\Diabetes\artifacts\Diabetes.pkl','rb'))

@app.route('/')
def main():
    return render_template('index.html')
@app.route('/predict',methods=['GET','POST'])
def predict():
    print(request.method)
    print('Hello world')
    if request.method=="GET":
        
        Pregnancies_var=int(request.form.get('Pregnancies',type=int))
        print(Pregnancies_var,type(Pregnancies_var))
        Glucose_var=int(request.form.get('Glucose'))
        BloodPressure_var=int(request.form.get('BloodPressure'))
        SkinThickness_var=int(request.form.get('SkinThickness'))
        Insulin_var=int(request.form.get('Insulin'))
        BMI_var=int(request.form.get('BMI'))
        DPF_var=int(request.form.get('DiabetesPedigreeFunction'))
        Age_var=int(request.form.get('Age'))
        result= model.predict([[Pregnancies_var,Glucose_var,BloodPressure_var,SkinThickness_var,Insulin_var,BMI_var,DPF_var,Age_var]])
        print("result>>",result)
        
        
    return result

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8080)

