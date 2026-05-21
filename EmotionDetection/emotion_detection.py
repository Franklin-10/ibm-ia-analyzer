import requests
import json

def emotion_detecter(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers = headers)
    formated = json.loads(response.text)
    emotions = formated['emotionPredictions'][0]['emotion']
    new_value = 0
    dominant_emotion = ''
    for emotion, value in emotions.items():
        if new_value < value:
            new_value = value
            dominant_emotion = emotion
    
    emotions['dominant_emotion'] = dominant_emotion
    return emotions


