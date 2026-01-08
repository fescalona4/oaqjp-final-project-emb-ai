# Emotion Detection Web Application

A Flask-based web application that analyzes text and detects emotions using IBM Watson's Natural Language Processing API. The application identifies five emotions (anger, disgust, fear, joy, sadness) and determines the dominant emotion in the provided text.

## Features

- **Emotion Detection**: Analyzes text input and detects five different emotions
- **Web Interface**: User-friendly web interface built with Bootstrap
- **RESTful API**: Provides an API endpoint for emotion detection
- **Real-time Analysis**: Instant emotion analysis results

## Project Structure

```
final-project/
├── EmotionDetection/
│   ├── __init.py__
│   └── emotion_detection.py    # Core emotion detection logic
├── static/
│   └── mywebscript.js          # Frontend JavaScript
├── templates/
│   └── index.html              # Web interface
├── server.py                   # Flask application server
├── test_emotion_detection.py   # Unit tests
├── Pipfile                     # Python dependencies
└── README.md                   # This file
```

## Prerequisites

- Python 3.14
- pipenv (for dependency management)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd final-project
```

2. Install dependencies using pipenv:
```bash
pipenv install
```

3. Activate the virtual environment:
```bash
pipenv shell
```

## Usage

### Running the Web Application

1. Start the Flask server:
```bash
python server.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

3. Enter text in the input field and click "Run Sentiment Analysis" to see the emotion detection results.

### API Endpoint

The application provides a REST API endpoint for emotion detection:

**Endpoint**: `/emotionDetector`

**Method**: GET

**Parameters**:
- `textToAnalyze` (required): The text to analyze for emotions

**Example Request**:
```
http://localhost:5000/emotionDetector?textToAnalyze=I am glad this happened
```

**Example Response**:
```json
{
    "anger": 0.0,
    "disgust": 0.0,
    "fear": 0.0,
    "joy": 0.5,
    "sadness": 0.0,
    "dominant_emotion": "joy"
}
```

## Testing

Run the unit tests to verify the emotion detection functionality:

```bash
python test_emotion_detection.py
```

The test suite validates that the emotion detector correctly identifies:
- Joy
- Anger
- Disgust
- Sadness
- Fear

## Dependencies

- **Flask**: Web framework for Python
- **requests**: HTTP library for API calls
- **pylint**: Code linting tool

All dependencies are specified in the `Pipfile`.

## How It Works

1. The user enters text through the web interface or sends a request to the API endpoint
2. The text is sent to IBM Watson's Emotion Prediction API
3. The API returns emotion scores for five emotions: anger, disgust, fear, joy, and sadness
4. The application determines the dominant emotion (the one with the highest score)
5. Results are returned to the user in JSON format

## License

See the LICENSE file for details.
