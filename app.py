from flask import Flask,render_template,request
from sklearn.pipeline import Pipeline
import numpy as np


import pickle

model = pickle.load(open('pipe.pkl','rb'))


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict_placement():
    limit=int(request.form.get('Limit'))
    gender=int(request.form.get('Gender'))
    education=int(request.form.get('Education'))
    marital_status=int(request.form.get('Marital status'))
    age=int(request.form.get('Age'))
    rep_sep=int(request.form.get('rep_sep'))
    rep_aug=int(request.form.get('rep_aug'))
    rep_july=int(request.form.get('rep_july'))
    rep_june=int(request.form.get('rep_june'))
    rep_may=int(request.form.get('rep_may'))
    rep_apr=int(request.form.get('rep_apr'))
    bs=int(request.form.get('bs'))
    ba=int(request.form.get('ba'))
    bjl=int(request.form.get('bjl'))
    bju=int(request.form.get('bju'))
    bm=int(request.form.get('bm'))
    bap=int(request.form.get('bap'))
    pay_sep=int(request.form.get('sep'))
    pay_aug=int(request.form.get('aug'))
    pay_july=int(request.form.get('july'))
    pay_june=int(request.form.get('june'))
    pay_may=int(request.form.get('may'))
    pay_april=int(request.form.get('apr'))

    list_column = [limit,gender,education,marital_status,age,rep_sep,rep_aug,rep_july,rep_june,rep_may,rep_apr,bs,ba,bjl,bju,bm,bap,pay_sep,pay_aug,pay_july,pay_june,pay_may,pay_april]
    
    #prediction
    
    result=model.predict(np.array(list_column).reshape(1,23))
    result = model.predict_proba(np.array(list_column).reshape(1,23))
    result = result.tolist()[0]
    
    #if result[0] == 1:
        #result = 'Defaulter'
    #else:
        #result = 'Not Defaulter'

    return render_template('index.html',result=(f'This Applicat has {round(result[0]*100,2)}% chances of Not Defaulting and {round(result[1]*100,2)}% chances of Defaulting'))
    #return render_template('index.html',result=result)
    
    #return str(result)
    

if __name__=='__main__':
    #app.run(host='0.0.0.0',port=8080)
    app.run(debug=True)
