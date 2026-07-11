# Emotion Detector

**Final Project: Emotion Detector**

A Python/Flask web application that uses the Watson NLP library to
detect the emotions (anger, disgust, fear, joy, sadness) expressed in
a piece of text and reports the dominant emotion.

## Project Structure
```
emotion_detector/
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
├── templates/
│   └── index.html
├── static/
│   └── mywebscript.js
├── server.py
├── test_emotion_detection.py
├── requirements.txt
└── README.md
```

## Setup
```bash
pip install -r requirements.txt
```

## Run the web app
```bash
python3 server.py
```
Then visit `http://localhost:5000` in your browser.

## Run unit tests
```bash
python3 -m unittest test_emotion_detection.py
```

## Run static code analysis
```bash
pylint server.py
```
