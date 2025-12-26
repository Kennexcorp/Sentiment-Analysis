from flask import Flask, request, render_template
import json
import requests



app = Flask(__name__)
app.config.from_file(".env.json", load=json.load)


@app.route("/", methods=['GET', 'POST'])
def sentiment():
    endpoint = app.config['ENDPOINT']
    key = app.config['LANGUAGE_SERVICE_KEY']
    
    if request.method == 'POST':
       
        text = request.get_json()['text']
        
        input = {'documents': [
            { 'id': '1000', 'text': text}
        ]}
        
        headers = {
            'Ocp-Apim-Subscription-Key': key,
            'Content-type': 'application/json'
        }
        endpoint = endpoint + 'text/analytics/v3.0/sentiment'
        response = requests.post(url=endpoint, headers=headers, json=input)
        results = response.json()['documents'][0]['confidenceScores']
        
        results = {
            "negative": results['negative'] * 100,
            "neutral": results['neutral'] * 100,
            "positive": results['positive'] * 100
        }
        
        return results
   
    
    return render_template('sentiment.html')