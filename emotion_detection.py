import json
import requests

def emotion_detector(text_to_analyze):
    """
    Function to detect emotions in text using Watson NLP library
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_data = { "raw_document": { "text": text_to_analyze } }
    
    # Send POST request to the Watson NLP API
    response = requests.post(url, headers=headers, json=input_data)
    
    # Parse the response JSON
    if response.status_code == 200:
        response_dict = json.loads(response.text)
        
        # Extract emotions from the response
        emotions = response_dict['emotionPredictions'][0]['emotion']
        
        # Find the dominant emotion (the one with highest score)
        dominant_emotion = max(emotions, key=emotions.get)
        
        # Format the output - ensure proper structure
        result = {
            'anger': emotions['anger'],
            'disgust': emotions['disgust'],
            'fear': emotions['fear'],
            'joy': emotions['joy'],
            'sadness': emotions['sadness'],
            'dominant_emotion': dominant_emotion
        }
        
        return result
    else:
        # Handle error cases
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }




