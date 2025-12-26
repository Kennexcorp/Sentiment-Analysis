# Sentiment Analysis App

A Flask-based web application that performs sentiment analysis on text using Azure Cognitive Services Language API.

## Description

This application provides a simple web interface for analyzing the sentiment of text input. It uses Azure Cognitive Services to determine whether the text is positive, negative, or neutral, and displays the confidence scores with animated progress bars.

## Features

- Web-based interface with responsive design using Tailwind CSS
- Real-time sentiment analysis via Azure Cognitive Services
- Visual representation of sentiment scores with progress bars
- Error handling for API failures
- Clean, modern UI with loading indicators

## Prerequisites

- Python 3.6+
- Azure Cognitive Services account with Language Service
- Valid subscription key and endpoint URL

## Installation

1. Clone or download this repository.

2. Install the required Python packages:
   ```
   pip install flask
   ```

3. Configure your Azure Cognitive Services credentials in `.env.json`:
   ```json
   {
       "TEXT_ANALYSIS_ENDPOINT": "https://your-resource-name.cognitiveservices.azure.com/",
       "TEXT_ANALYSIS_KEY": "your-subscription-key"
   }
   ```

## Usage

1. Run the Flask application:
   ```
   flask --app wintellect run
   ```

2. Open your web browser and navigate to `http://127.0.0.1:5000/`

3. Enter text in the textarea and click "Analyze Sentiment"

4. View the sentiment analysis results displayed as percentages with progress bars

## API Endpoint

The application exposes a REST API endpoint:

- **POST /** : Accepts JSON with a `text` field and returns sentiment confidence scores
  - Request: `{"text": "Your text here"}`
  - Response: `{"positive": 85.5, "negative": 10.2, "neutral": 4.3}`

## Configuration

Environment variables are loaded from `.env.json`:

- `ENDPOINT`: Your Azure Cognitive Services endpoint URL
- `LANGUAGE_SERVICE_KEY`: Your Azure subscription key

Ensure `.env.json` is in the root directory and not committed to version control (it's in `.gitignore`).

## Dependencies

- Flask: Web framework
- Requests: HTTP library for API calls
- Azure Cognitive Services Language API
- Tailwind CSS (via CDN)
- Axios (via CDN for AJAX requests)

## Contributing

Feel free to submit issues and enhancement requests.

## License

This project is open source. Please check the license file if available.
