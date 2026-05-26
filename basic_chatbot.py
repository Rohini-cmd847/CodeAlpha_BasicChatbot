def chatbot():
    print("=" * 50)
    print("            CODEALPHA SMART CHATBOT")
    print("=" * 50)
    print("Type 'help' to see commands.")
    print("Type 'exit' to end the chat.\n")

    name = input("Before we start, what's your name? ").strip()
    if name == "":
        name = "User"

    print(f"\nChatbot: Hello {name}! Nice to meet you.\n")

    responses = {
        "hello": f"Hi {name}! How can I help you today?",
        "hi": f"Hello {name}! Nice to see you.",
        "how are you": "I'm fine, thanks for asking!",
        "what is your name": "I am CodeAlpha Smart Chatbot.",
        "thank you": "You're welcome!",
        "thanks": "Anytime!",
        "bye": f"Goodbye {name}! Have a great day!"
    }

    while True:
        user_input = input("You: ").strip().lower()

        if user_input == "exit":
            print("Chatbot: Chat ended. See you soon!")
            break
        elif user_input == "help":
            print("\nChatbot Commands:")
            print("- hello")
            print("- hi")
            print("- how are you")
            print("- what is your name")
            print("- thank you")
            print("- bye")
            print("- exit\n")
        elif user_input in responses:
            print("Chatbot:", responses[user_input])
            if user_input == "bye":
                break
        elif user_input == "":
            print("Chatbot: Please type something.")
        else:
            print("Chatbot: Sorry, I don't understand that. Type 'help' for options.")

chatbot()
