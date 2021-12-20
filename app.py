from flask import Flask,request,render_template
import pandas as pd
import numpy as np
import pickle
pipe = pickle.load(open('bike.pkl','rb'))

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/predict', methods = ['POST'])
def predict():
    hour = int(request.form.get('hour'))
    temp = float(request.form.get('temp'))
    humi = float(request.form.get('humi'))
    wind = float(request.form.get('wind'))
    visi = float(request.form.get('visi'))
    dew = float(request.form.get('dew'))
    solar = float(request.form.get('solar'))
    rain = float(request.form.get('rain'))
    snow = float(request.form.get('snow'))
    season = str(request.form.get('season'))
    holi = str(request.form.get('holi'))
    #func = str(request.form.get('func'))
    month = str(request.form.get('month'))
    year = str(request.form.get('year'))
    week =  str(request.form.get('week'))

    

    list_column = [hour,temp,humi,wind,visi,dew,solar,rain,snow,season,holi,'Yes',month,year,week]
    data =pd.DataFrame(np.array([list_column]),columns=['Hour', 'Temperature(°C)', 'Humidity(%)', 'Wind speed (m/s)',
       'Visibility (10m)', 'Dew point temperature(°C)',
       'Solar Radiation (MJ/m2)', 'Rainfall(mm)', 'Snowfall (cm)', 'Seasons',
       'Holiday', 'Functioning Day', 'month', 'year', 'week'])

    result = pipe.predict(data)
    result = int(result[0])

    return render_template('index.html',result=str(f'You Need  {result}  Bikes'))

    
if __name__=="__main__":
    app.run(debug=True)
