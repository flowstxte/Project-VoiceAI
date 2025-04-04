import speech_recognition as sr
import pyttsx3
import sys
from app import AIAssistant

class VoiceAIAssistant:
    def __init__(self):
        # Initialize the recognizer and text-to-speech engine
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init('sapi5')
        
        # Initialize the AI assistant from app.py
        self.ai_assistant = AIAssistant()
        
        # Configure text-to-speech
        try:
            voices = self.engine.getProperty('voices')
            self.engine.setProperty('voice', voices[1].id)  # Female voice
            self.engine.setProperty('rate', 150)
            print("Voice AI Assistant initialized successfully")
        except Exception as e:
            print(f"Error initializing text-to-speech: {str(e)}")
            sys.exit(1)
            
        # Improve speech recognition accuracy
        self.recognizer.energy_threshold = 300  # Increase energy threshold for better noise handling
        self.recognizer.dynamic_energy_threshold = True  # Dynamically adjust for ambient noise
        self.recognizer.pause_threshold = 0.6  # Shorter pause detection for faster response
        
    def speak(self, text):
        """Convert text to speech"""
        print(f"AI: {text}")
        try:
            self.engine.say(text)
            self.engine.runAndWait()
        except Exception as e:
            print(f"Error in speech synthesis: {str(e)}")
    
    def listen(self):
        """Listen for user voice input with improved accuracy"""
        try:
            with sr.Microphone() as source:
                print("\nListening...")
                # Shorter noise adjustment for faster response
                self.recognizer.adjust_for_ambient_noise(source, duration=0.3)
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=10)
            
            try:
                # Using Google's speech recognition for better accuracy
                user_input = self.recognizer.recognize_google(audio, language='en-US')
                print(f"You said: {user_input}")
                return user_input
            except sr.UnknownValueError:
                self.speak("Sorry, I couldn't understand what you said.")
                return None
            except sr.RequestError as e:
                self.speak("Sorry, there was an error with the speech recognition service.")
                print(f"Speech recognition error: {str(e)}")
                return None
        except Exception as e:
            print(f"Error in listening: {str(e)}")
            return None
    
    def get_ai_response(self, user_input):
        """Get response from the AI assistant"""
        try:
            return self.ai_assistant.get_response(user_input)
        except Exception as e:
            print(f"Error getting response from AI: {str(e)}")
            return "I'm having trouble connecting to my brain right now."
    
    def run(self):
        """Run the voice assistant"""
        self.speak("Voice AI Assistant is ready. Ask me anything or say 'exit' to end the session.")
        
        while True:
            user_input = self.listen()
            
            if not user_input:
                continue
                
            # Check for exit command
            if user_input.lower() in ["exit", "quit", "stop", "goodbye"]:
                self.speak("Goodbye! Have a nice day.")
                break
            
            # Get response from AI assistant
            response = self.get_ai_response(user_input)
            self.speak(response)

if __name__ == "__main__":
    voice_assistant = VoiceAIAssistant()
    voice_assistant.run()
