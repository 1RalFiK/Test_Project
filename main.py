import requests

your_api_key = 'bac449ab-f338-4367-bcd9-28fd15ae6805'
AUDIO_FILE_PATH = 'https://www.dropbox.com/home/test?preview=Somesh.wav'
upload_url = 'https://api.fireflies.ai/graphql'
URL_file = 'https://www.dropbox.com/home/test?preview=Somesh.wav'


headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {your_api_key}'
}

data = {
    'query': 'mutation($input: AudioUploadInput) { uploadAudio(input: $input) { success title message } }',
    'variables': {
        'input': {
            'url': URL_file,
            'title': 'title of the file',
            'attendees': [

            ]
        }
    }
}

response = requests.post(upload_url, json = data, headers=headers,)
print(response.json())