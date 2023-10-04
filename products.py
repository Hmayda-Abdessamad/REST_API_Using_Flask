from flask import Flask,jsonify,request;

import json

app=Flask(__name__)

products=[
    {'id':143,'name':"notebook",'price':40},
    {'id':144,'name':"Black Marker",'price':10} 
]

@app.route('/products',methods=['GET'])

def getAllProducts():
    return jsonify(products)
