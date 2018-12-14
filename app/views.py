__author__ = 'IBM'

from app import app
import json
from flask import jsonify
from pprint import pprint

@app.route('/')

@app.route('/retJSON')

def retJSON():
    list = [
            {'Name': "Abhinav", 'Role': "Full Stack Developer",'Experience':"5+ years",'GitURL':"https://github.com/abhinav-dodda"},
            {'Name': "ABC", 'Role': "Front End Developer",'Experience':"3+ years",'GitURL':"https://github.com/"}
           ]
    return jsonify(ibmJSON = list)           

@app.route('/retHTML')

def retHTML():
    return "<h1> Welcome to IBM Security</h1>"    
