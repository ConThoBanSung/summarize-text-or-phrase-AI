import requests
import json

# Thay thế bằng API key hợp lệ từ Google Cloud Console
api_key = 'AIzaSyD1bCkgsZEZCaV3eJbb5Ec_ITAuDNOPG84'

# API endpoint của Gemini
api_url = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={api_key}'

def summarize_text(text):
    headers = {
        'Content-Type': 'application/json',
    }

    data = {
        'contents': [
            {
                'parts': [
                    {'text': f'Summarize the following text: {text}'}
                ]
            }
        ]
    }

    response = requests.post(api_url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        try:
            result = response.json()
            candidates = result['candidates']
            if candidates:
                return candidates[0]['content']['parts'][0]['text']
            else:
                return 'No summary generated'
        except KeyError as e:
            print(f"KeyError: {e}")
            print(f"Response JSON: {result}")
            return 'Failed to process request'
    else:
        print(f"Error: {response.status_code}")
        print(f"Response: {response.json()}")
        return 'Failed to process request'

if __name__ == '__main__':
    user_text = input("Enter the text you want to summarize: ")

    if user_text.strip():
        summary = summarize_text(user_text)
        print("\nSummary:")
        print(summary)
    else:
        print("No text provided")
