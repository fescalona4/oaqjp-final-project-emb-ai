import requests  
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }  # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers
    
    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)
    anger_score = formatted_response['emotionPredictions']['anger']
    disgust_score = formatted_response['emotionPredictions']['disgust']
    fear_score = formatted_response['emotionPredictions']['fear']
    joy_score = formatted_response['emotionPredictions']['joy']
    sadness_score = formatted_response['emotionPredictions']['sadness']
    dominant_emotion = formatted_response['emotionPredictions']['dominant_emotion']['label']
    # Returning a dictionary containing analysis results
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
        }