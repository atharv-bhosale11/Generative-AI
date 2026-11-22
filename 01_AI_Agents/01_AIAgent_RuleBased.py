print("Marvellous Infosystems")
print("Simple Rule Based AI Agent")

def simple_agent(user_input):
    user_input = user_input.lower()

    if "hello" in user_input:
        return "Hello! Welcome. How can I assist you today?"
    
    elif "weather" in user_input:
        return "I can help you with general weather-related queries."
    
    elif "time" in user_input:
        return "You can check your device clock for the current time."
    
    elif "help" in user_input:
        return "Sure! Tell me what you need help with."
    
    elif "bye" in user_input:
        return "Goodbye! Have a wonderful day."
    
      else:
        return "I'm sorry, I couldn't understand that. Please try another question."
  
while True:
    query = input("User: ")

    response = simple_agent(query)
    print("Agent:", response)

    if "bye" in query.lower():
        break
