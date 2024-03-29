import numpy as np
import pickle
import pandas
import os
from flask import Flask, request, render_template


app = Flask(__name__)
model = pickle.load(open(r'C:\Users\Manasa\OneDrive\Desktop\Major Project\xgb.pkl', 'rb'))
#scale = pickle.load(open(r'scale1.pkl','rb'))

@app.route('/') # rendering the html template
def home():
    return render_template('index.html')
@app.route('/inner-page') # rendering the html template
def output() :
    return render_template("inner-page.html")

@app.route('/submit',methods=["POST","GET"])# route to show the predictions in a web UI
def submit():
    #  reading the inputs given by the user
    # Convert non-empty values to floats
    input_feature = [float(x) for x in request.form.values() if x]

# Now you can use the float values as needed
  
    #input_feature = np.transpose(input_feature)
    input_feature=[np.array(input_feature)]
    print(input_feature)
    names = ['f','c','delta','PCA_Component']
    data = pandas.DataFrame(input_feature,columns=names)
    print(data)
    
    #data_scaled = scale.fit_transform(data)
    #data = pandas.DataFrame(,columns=names)

    

     # predictions using the loaded model file
    prediction=model.predict(data)
    print(prediction)
    out=prediction[0]
   
    
    return render_template("output.html",result = out)
    
     # showing the prediction results in a UI
if __name__=="__main__":
    
    app.run( port=8000,debug=True)    # running the app