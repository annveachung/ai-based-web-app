import requests  

def emotion_detector(text_to_analyse):  
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }  
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    try:
        response = requests.post(url, json=myobj, headers=header, timeout=10)
        response.raise_for_status()  # raises an HTTPError for bad responses (4xx/5xx)
        return response.text
    except requests.exceptions.Timeout:
        return {"error": "Request timed out"}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}