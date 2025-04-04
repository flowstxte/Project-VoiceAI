from openai import OpenAI
from config import OPENROUTER_API_KEY

class AIAssistant:
    def __init__(self):
        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=OPENROUTER_API_KEY,
        )
    
    def get_response(self, user_input):
        try:
            completion = self.client.chat.completions.create(
                model="deepseek/deepseek-r1:free",
                messages=[
                    {
                        "role": "user",
                        "content": user_input
                    }
                ]
            )
            
            response = completion.choices[0].message.content
            return response
            
        except Exception as e:
            return f"Error: {e}"

def main():
    assistant = AIAssistant()
    
    print("Voice AI Assistant (type 'exit' to quit)")
    print("-" * 50)
    
    while True:
        user_input = input("\nYou: ")
        
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        
        response = assistant.get_response(user_input)
        
        print("\nAssistant:")
        print("-" * 50)
        print(response)
        print("-" * 50)

if __name__ == "__main__":
    main()