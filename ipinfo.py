import requests

class IPInfoRes:
    def __init__(self, api_token):
        self.api_token = api_token

    def get_ipinfo(self, ip=None):
        base_url = "https://ipinfo.io/"
        
        if ip:
            url = f"{base_url}{ip}/json?token={self.api_token}"
        else:
            url = f"{base_url}json?token={self.api_token}"

        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            return None