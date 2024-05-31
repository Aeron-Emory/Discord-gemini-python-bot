## Try this Bot out
[![Static Badge](https://img.shields.io/badge/Replit-Try%20Here-orange?style=for-the-badge&logo=replit)
](https://replit.com/@AeronEmory/Discord-gemini-python-bot)

# A Discord Python Bot that interacts with Gemini API

"Python: Gemini Discord Bot" is a simple application that shows you how to interact with Google's Gemini APIs using pycord.

## Table of Contents

* [Directory contents](#directory-contents)
* [Setting up the API Key](#setting-up-the-api-key)
* [Getting started](#getting-started-with-vs-code)
* [Sign up for user research](#sign-up-for-user-research)

## Directory contents
* `main.py` - the Python application sends last 15 discord messages as prompt to Gemini API to generate content based on a prompt and send it back to the channel the bot's name as called
* `requirements.txt` - includes the google generative ai dependency and pycord

## Setting up the API Key
Before you can use the Gemini API, you must first obtain an API key. If you don't already have one, create a key with one click in Google AI Studio.
[Get API](https://makersuite.google.com/app/apikey) 
Check if Google AI Studio is available in [your region](https://ai.google.dev/available_regions)

## Run the application locally 

1. Make sure you have generated the API key as shown above. Please make sure to use and store this key securely. 

1. Install the package using 
```pip install -r requirements.txt```

1. Run this using 
```python main.py```

## Documentation 
1. You can see detailed API Reference for the Gemini APIs [here](https://ai.google.dev/gemini-api/docs) 

1. You can see more samples and things to do [here](https://googledevai.google.com/tutorials/python_quickstart)

1. You can see detailed Documentation for Pycord here [here](https://docs.pycord.dev/en/stable/)
