#!/usr/bin/env python

import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = makeWebhookResult(req)

    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def makeWebhookResult(req):
    if req.get("result").get("action") == "class-assignment":
      	result = req.get("result")
      	parameters = result.get("parameters")
      	zone = parameters.get("subjects")

      	cost = {'FLAT':'20th April', 'Software':'5th May', 'Algorithms':1, 'COA':1}
	
      	if cost[zone] != 1:
        	speech = "The deadline for " + zone + " assignment is " + str(cost[zone]) + "."
      	if cost[zone] == 1:
        	speech = "The assignment for " + zone + " is done""."

      	print("Response:")
      	print(speech)

      	return {
          	"speech": speech,
          	"displayText": speech,
          	#"data": {},
          	# "contextOut": [],
          	"source": "apiai-onlinestore-shipping"
      	}
        
    elif req.get("result").get("action") == "class.timings":
      	result = req.get("result")
      	parameters = result.get("parameters")
      	zone = parameters.get("timings-relative")

      	cost = {'today': 1 , 'tomorrow': 2}
      	calendarfortoday = {"Algorithms" : "10 AM" , "COA" : "11 AM", "Software" : "9 AM"}
	    calendarfortomorrow = {"Algorithms" : "9 AM" , "COA" : "10 AM", "Software" : "11 AM"}
    
      	if cost[zone] == 1:
        	speech = "The timetable for " + zone + " is " + str(calendarfortoday["Software"]) + "\n" + 
        												str(calendarfortoday["Algorithms"]) + "\n" +
        												str(calendarfortoday["COA"]) + " . "
      	if cost[zone] != 1:
         	speech = "The timetable for " + zone + " is " + str(calendarfortomorrow["algorithms"]) + "\n" + 
        												str(calendarfortomorrow["COA"]) + "\n" +
        												str(calendarfortomorrow["Software"]) + " . "
      	print("Response:")
      	print(speech)

      	return {
          	"speech": speech,
          	"displayText": speech,
          	#"data": {},
          	# "contextOut": [],
          	"source": "apiai-onlinestore-shipping"
        }
    else: return {}

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print "Starting app on port %d" % port

    app.run(debug=True, port=port, host='0.0.0.0')
