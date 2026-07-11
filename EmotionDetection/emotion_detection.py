"""
emotion_detection.py

Uses the Watson NLP EmotionPredict service to analyze the emotional
content of a piece of text and returns a formatted dictionary of
emotion scores plus the dominant emotion.
"""

import json
import requests


def emotion_detector(text_to_analyze):
    """
    Sends text to the Watson NLP EmotionPredict API and returns a
    dictionary containing the scores for anger, disgust, fear, joy,
    sadness, and the dominant emotion.

    If the input text is blank/invalid, the API returns a 400 status
    code and this function returns a dictionary with all values set
    to None (Task 7 - error handling).
    """
    url = (
        'https://sn-watson-emotion.labs.skills.network/v1/'
        'watson.runtime.nlp.v1/NlpService/EmotionPredict'
    )
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    input_json = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, json=input_json, headers=headers)

    # Task 7: handle blank/invalid input -> status code 400
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotionPredictions'][0]['emotion']

    anger = emotions['anger']
    disgust = emotions['disgust']
    fear = emotions['fear']
    joy = emotions['joy']
    sadness = emotions['sadness']

    emotion_scores = {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness
    }

    # Task 3: dominant emotion is whichever key has the highest score
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
    }
