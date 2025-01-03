def chatbot_response(user_input):
    responses = {
        "hi": "Hello! How can I assist you today?",
        "hello": "Hi there! What can I do for you?",
        "how are you": "I'm just a computer program, but thanks for asking!",
        "what is your name": "I am a simple chatbot created to assist you.",
        "bye": "Goodbye! Have a nice day!",
    }
    user_input = user_input.lower()


    return responses.get(user_input, "I'm sorry, I don't understand that.")

def chatbot():
    print("Hi! I'm a simple chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye! Have a nice day!")
            break
        
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")


if __name__ == "__main__":
    chatbot()
