import requests
import json

# Define the API endpoint URL
api_url = "http://localhost:5000/query"  # Replace with the actual URL of your API

# Define the question you want to query
question = "How to use the gunion command in FreeBSD?"

# Create a JSON payload with the question
payload = {"question": question}

# Send a POST request to the API
response = requests.post(api_url, json=payload)

# Check the response status code
if response.status_code == 200:
    # Parse and print the response
    data = response.json()
    print("Question:", data["question"])
    print("Related Chunks:")
    for chunk in data["related_chunks"]:
        print(chunk)
else:
    print(f"Error: {response.status_code}")
    print(response.text)
