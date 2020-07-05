from flask import Flask, jsonify
from firebase import firebase
import json 
firebase=firebase.FirebaseApplication('https://do-an-cuoi-ky-n9.firebaseio.com/')
def findNextTempAfter30Minutes(x,y):
    return (0.777413*float(x)+0.026063*float(y)+4.776435100864418)
def findNextTempAfter60Minutes(x,y):
    return (-0.677189*float(x)+0.184789*float(y)+41.81936890229139)
def findNextTempAfter90Minutes(x,y):
    return (-0.350735*float(x)+0.238915*float(y)+27.14063270633815)
# EB looks for an 'application' callable by default.
application = Flask(__name__)

# add a rule for the index page.

# add a rule when the page is accessed with a name appended to the site
# URL.

@application.route('/',methods=['GET'])
def homePage():
    resultJsonTemperature=firebase.get('/DHT11/Temperature',None)
    resultJsonHumidity=firebase.get('/DHT11/Humidity',None)
    temperature=[]
    for key, value in resultJsonTemperature.items():
        temperature.append(float(value))
    humidity=[]
    for key, value in resultJsonHumidity.items():
        humidity.append(float(value))
    cur=temperature[-1]
    return jsonify({'current':cur})
@application.route('/iot30Minutes',methods=['GET'])
def getNext30FromCurrent():
    resultJsonTemperature=firebase.get('/DHT11/Temperature',None)
    resultJsonHumidity=firebase.get('/DHT11/Humidity',None)
    temperature=[]
    for key, value in resultJsonTemperature.items():
        temperature.append(float(value))
    humidity=[]
    for key, value in resultJsonHumidity.items():
        humidity.append(float(value))
    cur=temperature[-1]
    humid=humidity[-1]
    next_temp=findNextTempAfter30Minutes(cur,humid)
    return jsonify({'current':cur,'next':next_temp})
@application.route('/iot60Minutes',methods=['GET'])
def getNext60FromCurrent():
    resultJsonTemperature=firebase.get('/DHT11/Temperature',None)
    resultJsonHumidity=firebase.get('/DHT11/Humidity',None)
    temperature=[]
    for key, value in resultJsonTemperature.items():
        temperature.append(float(value))
    humidity=[]
    for key, value in resultJsonHumidity.items():
        humidity.append(float(value))
    cur=temperature[-1]
    humid=humidity[-1]
    next_temp=findNextTempAfter60Minutes(cur,humid)
    return jsonify({'current':cur,'next':next_temp})
@application.route('/iot90Minutes',methods=['GET'])
def getNext90FromCurrent():
    resultJsonTemperature=firebase.get('/DHT11/Temperature',None)
    resultJsonHumidity=firebase.get('/DHT11/Humidity',None)
    temperature=[]
    for key, value in resultJsonTemperature.items():
        temperature.append(float(value))
    humidity=[]
    for key, value in resultJsonHumidity.items():
        humidity.append(float(value))
    cur=temperature[-1]
    humid=humidity[-1]
    next_temp=findNextTempAfter90Minutes(cur,humid)
    return jsonify({'current':cur,'next':next_temp})
@application.route('/iot/<float:temp>',methods=['GET'])
def getNext(temp):
    next_temp=findNextTempAfter30Minutes(temp,70)
    return jsonify({'next':next_temp})
# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()