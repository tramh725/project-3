from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

mongo= MongoClient(port=27017)
db=mongo.usdemo

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/age", methods=["GET"])