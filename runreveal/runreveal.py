import os
import requests
import pandas as pd
from base64 import b64encode
import json

API_URL = "https://api.runreveal.com/logs/query"

WORKSPACE_ID = os.getenv("RUNREVEAL_WORKSPACE")
AUTH_TOKEN = os.getenv("RUNREVEAL_AUTH_TOKEN")

class RunReveal:
    def __init__(self, query, useai=False):
        self.query = query
        self.useai = useai
        self.resp = self.logs()
        self.columns = self.resp['result']['columns']
        self.values = self.resp['result']['values']
        self.rows = self.get_rows()

        
    def logs(self):
        if not WORKSPACE_ID:
            raise ValueError("RUNREVEAL_WORKSPACE environment variable not set!")
        if not AUTH_TOKEN:
            raise ValueError("RUNREVEAL_AUTH_TOKEN environment variable not set!")
    
        headers = {
            "Authorization": f"Basic {AUTH_TOKEN}"
        }
    
        payload = {
            "query": self.query,
            "useai": self.useai,
            "source": "jupyter",
            "parameters": {}
        }
    
        response = requests.post(f"{API_URL}?workspaceid={WORKSPACE_ID}", json=payload, headers=headers)

        robj = json.loads(response.text)
        if response.status_code != 200:
            raise ValueError(f"Error: {robj['error']}")
        if robj['success'] != True:
            raise ValueError(f"Error: {robj['error']}")

        return robj

    def get_rows(self):
        transposed_values = list(zip(*self.values))  # Transposing the list of lists
        return [dict(zip(self.columns, row)) for row in transposed_values]
    
    def create_dataframe(self):
        return pd.DataFrame(list(zip(*self.values)), columns=self.columns)

