import json

def load_data_from_json(file: str):
    with open(file, 'r') as f:
        data = json.load(f)
        return data