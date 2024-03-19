from flask import request, jsonify
from .utils import refresh_access_token, post_data_to_zoho

def init_app(app):
    @app.route('/api/data', methods=['POST'])
    def receive_data():
        if request.is_json:
            data = request.get_json()
            print("Received data:", data)
            # Refresh access token if necessary
            refresh_access_token()
            # Post data to Zoho Creator API
            post_data_to_zoho(data)
            return jsonify({"message": "Data received and processed successfully"}), 200
        else:
            return jsonify({"error": "Invalid content type. Please send JSON data."}), 400
