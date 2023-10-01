import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers = header)
    formatted_response = json.loads(response.text)
    if response.status_code == 200:
        anger_score = float(formatted_response['emotionPredictions'][0]['emotion']['anger'])
        disgust_score = float(formatted_response['emotionPredictions'][0]['emotion']['disgust'])
        fear_score = float(formatted_response['emotionPredictions'][0]['emotion']['fear'])
        joy_score = float(formatted_response['emotionPredictions'][0]['emotion']['joy'])
        sadness_score = float(formatted_response['emotionPredictions'][0]['emotion']['sadness'])
    elif response.status_code == 400:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
    resultsobj = {'anger': anger_score,'disgust': disgust_score,'fear': fear_score,'joy': joy_score,'sadness': sadness_score }
    basescore = 0
    emotion = 'something'
    if response.status_code == 200:
        for key in resultsobj:
            if resultsobj[key] >= basescore:
                basescore = resultsobj[key]
                emotion = key
        resultsobj['dominant_emotion'] = emotion
    if response.status_code == 400:
        resultsobj['dominant_emotion'] = None
    return resultsobj
