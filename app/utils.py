import requests
import json

# Replace these with your actual tokens and credentials
refresh_token = "1000.1ebfe1d8c6e1c5ac74e1cbc39a2c0c2c.9b0ad7cece74c6367138822fff035b47"
client_id = "1000.RVJPPOEJD3YAH5451WOWGKD4U0UV9F"
client_secret = "79918d8d68d00bd44f750432cae9a571d513b4c03b"
access_token = "1000.f4ae553e6c57abb2cfd826244285a239.ebf7670fd1595dd3f04bc9e9ca40f5d9"

# Zoho API endpoints
token_endpoint = "https://accounts.zoho.in/oauth/v2/token"
zoho_api_endpoint = "https://creator.zoho.in/api/v2.1/admin_kaderiambalmills1/packing-material-requirement/form/Itemsdetails"

def refresh_access_token():
    global access_token
    payload = {
        "refresh_token": refresh_token,
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "refresh_token"
    }
    response = requests.post(token_endpoint, data=payload)
    if response.status_code == 200:
        response_data = response.json()
        access_token = response_data.get("access_token")
        print("Access token refreshed successfully.")
    else:
        print("Failed to refresh access token.")

def post_data_to_zoho(data):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}"
    }
    response = requests.post(zoho_api_endpoint, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        print("Data posted to Zoho Creator successfully.")
    else:
        print("Failed to post data to Zoho Creator.")
