from flask import Flask, request, jsonify
import boto3
import pandas as pd
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return '''<h1><center>Comprehend Test'''

@app.route('/SA', methods=['GET'])
def Perform_SentimetnAnalysis():
    notes='This is good to do testing on comprehend for sentiment analysis.'
    client = boto3.client(service_name='comprehend')
    sentiment_output = client.detect_sentiment(Text=notes, LanguageCode='en')
    return sentiment_output

if __name__ == '__main__':
    app.run(debug=True)