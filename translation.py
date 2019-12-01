import requests
import json
import time


def get_translate(text, from_lang, to_lang):
    timestamp = str(time.time())
    parameters = {
        "id" : "20260020",
        "jsonrpc": "2.0",
        "method": "LMT_handle_jobs",
        "params": {
            "jobs": [
                {
                    "kind": "default",
                    "raw_en_sentence": text,
                },
            ],
            "lang": {
                "user_preferred_langs": [
                    from_lang,
                    to_lang,
                ],
                "source_lang_user_selected": from_lang,
                "target_lang": to_lang,
            },
            "priority": "-1",
            "timestamp": timestamp,
        },
    }
    
    response = requests.post("https://www2.deepl.com/jsonrpc", json=parameters).json()
    
    return response["result"]["translations"][0]["beams"][0]["postprocessed_sentence"]
