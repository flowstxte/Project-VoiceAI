# Voice AI Assistant

A voice-controlled AI assistant that uses speech recognition to listen to your commands and questions, processes them using the DeepSeek AI model via OpenRouter API, and responds with a natural-sounding female voice.

## Features

- Voice input using speech recognition
- Natural-sounding female voice output
- Powered by DeepSeek AI model via OpenRouter
- Simple and intuitive interface
- Easy exit commands ("exit", "quit", "stop", "goodbye")

## Files

- `voice.py`: Handles speech recognition and text-to-speech functionality
- `app.py`: Manages communication with the OpenRouter API
- `config.py`: Stores your OpenRouter API key

## Requirements

- Python 3.7+
- Internet connection for speech recognition and AI responses

## Installation

### 1. Clone this repository or download the files

```bash
git clone https://github.com/flowstxte/Project-VoiceAI.git
cd voice-ai-assistant
```

### 2. Install the required packages

```bash
pip install openai SpeechRecognition pyttsx3 pyaudio
```

#### Note: Installing `pyaudio` might be challenging on some systems. If you encounter issues:

- **Windows**:
  ```bash
  pip install pipwin
  pipwin install pyaudio
  ```
- **macOS**:
  ```bash
  brew install portaudio
  pip install pyaudio
  ```
- **Linux**:
  ```bash
  sudo apt-get install python3-pyaudio
  ```

## Getting an OpenRouter API Key

1. Create a free account at [OpenRouter](https://openrouter.ai)
2. After logging in, navigate to the "API" tab in the dashboard
3. Click the "Create API Key" button
4. Give your key a name (e.g., "Voice AI Assistant")
5. Copy the generated API key
6. Open `config.py` and replace the placeholder with your new key:

```python
OPENROUTER_API_KEY = "your_api_key_here"
```

## Usage

### Run the voice assistant

```bash
python voice.py
```

- Wait for the "Voice AI Assistant is ready" message
- Speak your question or command
- Listen to the AI's response
- To exit, say "exit", "quit", "stop", or "goodbye"

## How It Works

1. The application listens for your voice input using the microphone
2. Your speech is converted to text using Google's speech recognition service
3. The text is sent to the DeepSeek AI model via OpenRouter API
4. The AI generates a response
5. The response is converted to speech and played through your speakers

## Troubleshooting

- **Microphone not working**: Ensure your microphone is properly connected and set as the default input device
- **"Could not understand what you said"**: Try speaking more clearly or in a quieter environment
- **API errors**: Verify your API key is correct and that you have an active internet connection
- **Text-to-speech issues**: Ensure your speakers are working and not muted
