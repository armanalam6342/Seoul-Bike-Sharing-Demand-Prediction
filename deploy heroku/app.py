from flask import Flask,request,render_template
import numpy as np
import pickle
pipe = pickle.load(open('bike.pkl','rb'))

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

if __name__=="__main__":
    app.run()
