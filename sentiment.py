from flask import Flask, request, render_template
import json
import requests



app = Flask(__name__)
app.config.from_file(".env.json", load=json.load)


@app.route("/", methods=['GET', 'POST'])
def sentiment():
    endpoint = app.config['TEXT_ANALYSIS_ENDPOINT']
    key = app.config['TEXT_ANALYSIS_KEY']
    
    if request.method == 'POST':
        text = request.get_json()['text']
        documents =  [
            { 'id': '1000', 'text': text}
        ]
        # results = without_sdk_lib(endpoint, key, documents)
        results = with_sdk_lib(endpoint, key, documents)
        
        return {
            "negative": results['negative'] * 100,
            "neutral": results['neutral'] * 100,
            "positive": results['positive'] * 100
        }
   
    
    return render_template('sentiment.html')

def with_sdk_lib(endpoint, key, documents):
    from azure.core.credentials import AzureKeyCredential
    from azure.ai.textanalytics import TextAnalyticsClient
    from azure.core.exceptions import AzureError
    
    try:
        client = TextAnalyticsClient(endpoint, AzureKeyCredential(key))
        response = client.analyze_sentiment(documents)
        results = response[0]
        
    except AzureError as e:
        print("error occured", e.message)
    
    return {
            "negative": results.confidence_scores.negative,
            "neutral": results.confidence_scores.neutral,
            "positive": results.confidence_scores.positive
        }
def without_sdk_lib(endpoint, key, documents):
        
    input = {
        'documents': documents
    }
        
    headers = {
            'Ocp-Apim-Subscription-Key': key,
            'Content-type': 'application/json'
        }
    print(input)
    endpoint = endpoint + 'text/analytics/v3.0/sentiment'
    response = requests.post(url=endpoint, headers=headers, json=input)
    
    results = response.json()['documents'][0]['confidenceScores']
    
    return results