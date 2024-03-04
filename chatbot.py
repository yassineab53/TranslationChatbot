from googletrans import Translator
#  yassine abbou 
class TranslationChatbot:
    def __init__(self):
        self.translator = Translator()

    def translate_text(self, text, target_language='en'):
        translation = self.translator.translate(text, dest=target_language)
        return translation.text

    def chat(self):
        print("Translation Chatbot: Hello! I'm here to help you with translations. Type 'exit' to end the chat.")
        
        while True:
            user_input = input("You: ")
            
            if user_input.lower() == 'exit':
                print("Translation Chatbot: Goodbye! Have a great day.")
                break
            
            target_language = input("Enter target language (e.g., 'fr' for French): ")
            
            translated_text = self.translate_text(user_input, target_language)
            
            print(f"Translation Chatbot: {translated_text}")

if __name__ == "__main__":
    chatbot = TranslationChatbot()
    chatbot.chat()
