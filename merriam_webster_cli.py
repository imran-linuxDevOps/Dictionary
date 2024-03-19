# merriam_webster_cli.py

import requests
import sys
import warnings

# Suppress the warning related to OpenSSL version
warnings.filterwarnings("ignore", category=NotOpenSSLWarning)

def get_definition(word):
    api_key = "Put Your API Key Here"  # Replace this with your Merriam-Webster API key
    url = f"https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if isinstance(data, list):
            return data[0]["meta"]["stems"][0], data[0]["fl"], data[0]["shortdef"][0]
        else:
            return None
    else:
        print("Error:", response.status_code)
        return None

def format_response(word, pronunciation, part_of_speech, definition):
    return f"{word} ({pronunciation}) ({part_of_speech}): {definition}"

def main():
    if len(sys.argv) != 2:
        print("Usage: python merriam_webster_cli.py <word>")
        sys.exit(1)

    word = sys.argv[1]
    result = get_definition(word)
    if result:
        pronunciation, part_of_speech, definition = result
        print(format_response(word, pronunciation, part_of_speech, definition))
    else:
        print("Definition not found for the word:", word)

if __name__ == "__main__":
    main()
