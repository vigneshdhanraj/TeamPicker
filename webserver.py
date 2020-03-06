from flask import Flask, render_template, request
import sys
import json
abspath = "/home/dhanraj/Project/TeamPicker/"
sys.path.append(abspath)
from teampicker import Getteam
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Getplaylist', methods = ['POST'])
def getplayerlist():
    team1_list = []
    team2_list = []
    if request.method == "POST":
    	pls = json.loads(request.data)
	var = raw_input("Please Enter File Name: ")
	var = abspath + var + ".json"
	print(var)
	with open(var, "w") as f:
	    json.dump(pls, f, indent=4)
	Getteam().worker(var)
    return "Success"

if __name__ == '__main__':
    app.run(debug=True, port=5000)
