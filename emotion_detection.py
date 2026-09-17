import requests
import json

def emotion_detector(text_to_analyse):  
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict' 
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)
    formatted_response = json.loads(response.text)
    emotions = formatted_response ['emotionPredictions'][0]['emotion']

    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']

    highest_score = max(anger_score,disgust_score,fear_score,joy_score,sadness_score)

    if highest_score == anger_score:
        dominant_emotion = 'anger'
    elif highest_score == disgust_score:
        dominant_emotion = 'disgust'
    elif highest_score == fear_score:
        dominant_emotion = 'fear'
    elif highest_score == joy_score:
        dominant_emotion = 'joy'
    else:
        dominant_emotion = 'sadness'

    return {
'anger': anger_score,
'disgust': disgust_score,
'fear': fear_score,
'joy': joy_score,
'sadness': sadness_score,
'dominant_emotion': dominant_emotion
}
