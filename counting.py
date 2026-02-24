
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        break
    elif message == 'parrot':
        print("Oh, think you're a wise guy huh?")
        break
    else:
        print(message)
