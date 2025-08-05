## 🎙️ Alexa - Voice Assistant in Python

A voice-controlled assistant built using Python that can perform tasks such as:
- Opening popular websites
- Playing your favorite music
- Fetching and reading current news
- Responding to custom voice commands

This assistant uses speech recognition, text-to-speech, and web automation to create a simple yet powerful personal assistant.

---

## 🚀 Features

- 🎧 Voice activation using wake word ("Alexa")
- 🎵 Music playback via browser using a song dictionary
- 📰 Read latest news headlines from NewsAPI
- 🌐 Open websites like YouTube, GitHub, Facebook, etc.

---


## 🛠️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/abhishek-gupta-24/voice_assistant.git
cd ALEXA
```

### 2. Create and Activate Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```
### 3. Install Required Packages
```bash
pip install -r requirements.txt
```

### 4. Add Your API Key
```bash 
Create a .env file in the root directory and paste your NewsAPI key:
```


### 📁 Project Structure

```
ALEXA/
├── API.py             # Loads API key from .env
├── main.py            # Main script to run the assistant
├── musicLibrary.py    # Dictionary of songs and YouTube links
├── requirements.txt   # Python dependencies
├── .env               # Stores API keys (not pushed to GitHub)
├── .gitignore         # Ignores sensitive and unnecessary files
```


### 📦 Dependencies
```
Dependencies are listed in requirements.txt. To install them:
pip install -r requirements.txt

```
