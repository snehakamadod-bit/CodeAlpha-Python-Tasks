def get_bot_response(user_message):
    user_message = user_message.lower().strip()

    if user_message == "hello":
        return "Hi!"
    elif user_message == "how are you":
        return "I'm fine, thanks!"
    elif user_message == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I do not understand that yet."


print("Chatbot: Hi! Type hello, how are you, or bye.")

while True:
    user_message = input("You: ")

    bot_response = get_bot_response(user_message)
    print("Chatbot:", bot_response)

    if user_message.lower().strip() == "bye":
        break