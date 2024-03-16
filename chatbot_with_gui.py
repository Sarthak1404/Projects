# Import the random module
import random
# Import the libraries
import tkinter as tk

# Define a dictionary of responses for different intents
responses = {
  "greet": ["Hello, I am a Buddy.", "Hi, nice to meet you.", "Greetings, how are you?"],
  "name": ["My name is Buddy.", "You can call me Buddy.", "I go by the name Buddy."],
  "age": ["I am as old as you want me to be.", "Age is just a number for me.", "I don't have a specific age."],
  "bye": ["Goodbye, have a nice day.", "See you later, take care.", "Bye, hope to talk to you again."],
  # more intent added
  "weather": ["The weather today is sunny and warm.", "It's cloudy and rainy right now.", "There is a chance of snow later."],
  "joke": ["What do you call a fish that wears a bowtie? Sofishticated.", "How do you make a tissue dance? You put a little boogie in it.", "Why did the chicken go to the seance? To get to the other side."],
  "fact": ["Did you know that the longest word in English is pneumonoultramicroscopicsilicovolcanoconiosis?", "Did you know that the unicorn is the national animal of Scotland?", "Did you know that octopuses have three hearts?"],
  "feedback": ["Thank you for your feedback. We appreciate your opinion.", "We are sorry to hear that you are not satisfied. Please let us know how we can improve.", "We are glad that you enjoyed our service. Please share your experience with others."],
  "hobby": ["That's a nice hobby. How long have you been doing it?", "That sounds interesting. What do you like most about it?", "That's cool. I wish I could do that too."],
  # more intent added
  "wellbeing": ["I'm sorry to hear that you are feeling this way. Do you want to talk about it?", "You are not alone. Many people struggle with their mental health. What can I do to help you?", "It's okay to feel sad or angry sometimes. These are normal human emotions. How do you usually cope with them?","What is causing you stress?", "Stress is a normal reaction to challenging situations.", "You can cope with stress by breathing deeply, talking to someone, or doing something you enjoy."],
  "mood": ["How are you feeling today?", "I hope you are in a good mood.", "Your mood affects your thoughts and actions.",],
  "self-esteem": ["How do you see yourself?", "You are a valuable and unique person.", "You can boost your self-esteem by acknowledging your strengths, accepting your flaws, and challenging your negative thoughts."],
  "gratitude": ["What are you grateful for?", "Gratitude can make you happier and healthier.", "You can practice gratitude by writing down three things you are thankful for every day."],
  "goal": ["What is your goal?", "A goal is a specific and measurable outcome that you want to achieve.", "You can reach your goal by breaking it down into smaller steps, tracking your progress, and celebrating your achievements."]
}

# Define a function to get the intent of the user's message
def get_intent(message):
  # Convert the message to lowercase
  message = message.lower()
  # Check if the message contains any of the keywords for each intent
  if "hello" in message or "hi" in message or "hey" in message:
    return "greet"
  elif "name" in message or "who" in message:
    return "name"
  elif "age" in message or "how old" in message:
    return "age"
  elif "bye" in message or "see you" in message or "quit" in message:
    return "bye"
  elif "weather" in message or "how is" in message or "what's" in message:
    return "weather"
  elif "joke" in message or "tell me" in message or "make me laugh" in message:
    return "joke"
  elif "fact" in message or "tell me something" in message or "did you know" in message:
    return "fact"
  elif "feedback" in message or "i think" in message or "i feel" in message:
    return "feedback"
  elif "hobby" in message or "i like" in message or "i enjoy" in message:
    return "hobby"
  elif "stress" in message or "anxiety" in message or "depression" in message or "i'm" in message or "pressure" in message: 
    return "wellbeing"
  elif "mood" in message or "feelings" in message or "emotion" in message:
    return "mood"
  elif "self-esteem" in message or "confidence" in message or "worth" in message:
    return "self-esteem"
  elif "gratitude" in message or "thankful" in message or "appreciate" in message:
    return "gratitude"
  elif "goal" in message or "aim" in message or "objective" in message:
    return "goal"
  else:
    return "unknown"

# Define a function to get a response for the user's message
def get_response(message):
  # Get the intent of the message
  intent = get_intent(message)
  # If the intent is known, choose a random response from the dictionary
  if intent in responses:
    return random.choice(responses[intent])
  # If the intent is unknown, say that the chatbot does not understand
  else:
    return "Sorry, I don't understand what you mean."

# Define a new light blue and purple color scheme
background_color = "#A01FE7"     # Veronica
text_area_color = "#C0DCF7"      # Columbia Blue
button_color = "#C0DCF7"         # Columbia Blue
text_color = "#301934"           # Dark Purple

# Create a root window with a title and set the background color
root = tk.Tk()
root.title("Chatbot Buddy")
root.configure(bg=background_color)

# Create a frame for the conversation area and scrollbar
conversation_frame = tk.Frame(root, bg=background_color)
conversation_frame.pack(pady=(10, 0))

# Create a text area for displaying the conversation with the color scheme
conversation = tk.Text(conversation_frame, width=75, height=20, bg=text_area_color, fg=text_color)
conversation.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create a scrollbar and attach it to the conversation text area
scrollbar = tk.Scrollbar(conversation_frame, command=conversation.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Configure the conversation text area to use the scrollbar
conversation.config(yscrollcommand=scrollbar.set)

# Create a frame for the input area and button
input_frame = tk.Frame(root, bg=background_color)
input_frame.pack(pady=(10, 10))

# Create an input field for the user to enter their message with the color scheme
user_input = tk.Entry(input_frame, width=58, bg=button_color, fg=text_color)
user_input.pack(side=tk.LEFT, padx=(0, 10))

# Define a function to handle the user's message
def send_message(event=None):
    # Get the user's message from the input field
    message = user_input.get()
    # Clear the input field
    user_input.delete(0, tk.END)
    # Insert the user's message into the conversation
    conversation.insert(tk.END, "You: " + message + "\n")
    # If the user types 'quit', break the loop
    if message.lower() == "quit":
        conversation.insert(tk.END, "Bye!!\n")
        root.after(1500, root.destroy)
    else:
        # Placeholder for the get_response function
        response = get_response(message)
        # Insert the chatbot's response into the conversation
        conversation.insert(tk.END, "Buddy: " + response + "\n")

# Create a button for sending the message with the color scheme
send_button = tk.Button(input_frame, text="Send", command=send_message, bg=button_color, fg=text_color)
send_button.pack(side=tk.RIGHT)

# Bind the Enter key to the send_message function
root.bind('<Return>', send_message)

# Start the chatbot conversation with a welcome message
conversation.insert(tk.END, "Welcome to the chatbot. Type 'quit' to exit.\n")

# Start the main loop
root.mainloop()