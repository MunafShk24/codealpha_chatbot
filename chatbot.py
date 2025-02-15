import nltk
import random
import string
import re

# Download NLTK resources
nltk.download('punkt')
nltk.download('wordnet')

# Preprocessing functions
def preprocess_input(user_input):
    # Lowercase the input
    user_input = user_input.lower()
    # Remove punctuation
    user_input = re.sub(f'[{string.punctuation}]', '', user_input)
    return user_input

# Sample responses
responses = {
    "greeting": ["Hello! How can I assist you today?", "Hi there! What can I do for you?", "Greetings! How may I help you?"],
    "goodbye": ["Goodbye! Have a great day!", "See you later!", "Take care!"],
    "thanks": ["You're welcome!", "No problem!", "Happy to help!"],
    "default": ["I'm sorry, I didn't understand that.", "Could you please rephrase?", "I'm not sure how to respond to that."]
}

# Function to get a response based on user input
def get_response(user_input):
    user_input = preprocess_input(user_input)
    
    if "hello" in user_input or "hi" in user_input:
        return random.choice(responses["greeting"])
    elif "bye" in user_input or "goodbye" in user_input:
        return random.choice(responses["goodbye"])
    elif "thank" in user_input:
        return random.choice(responses["thanks"])
    else:
        return random.choice(responses["default"])

# Main chatbot loop
def chatbot():
    print("Chatbot: Hi! I'm a chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "exit", "quit"]:
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = get_response(user_input)
        print(f"Chatbot: {response}")

# Run the chatbot
if __name__ == "__main__":
    chatbot()