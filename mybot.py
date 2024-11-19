import tkinter as tk
from tkinter import scrolledtext
import google.generativeai as ai

# Configure the Google Generative AI
# Add your API key here
API_KEY = "YOUR_API_KEY_HERE"  # Replace with your own API key from Google Generative AI
ai.configure(api_key=API_KEY)
model = ai.GenerativeModel("gemini-pro")
chat = model.start_chat()

# Initialize the main window
root = tk.Tk()
root.title("AI Chatbot")
root.geometry("500x600")
root.configure(bg="#2c3e50")

# Chat display area
chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, state="disabled", bg="#34495e", fg="white", font=("Arial", 12))
chat_display.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# User input field
user_input = tk.Entry(root, font=("Arial", 14), bg="#ecf0f1", fg="#333")
user_input.pack(fill=tk.X, padx=10, pady=(0, 5))

# Function to Add Message to Chat Display
def add_message_to_chat(message, sender="You"):
    chat_display.config(state="normal")
    chat_display.insert(tk.END, f"{sender}: {message}\n\n")
    chat_display.config(state="disabled")
    chat_display.see(tk.END)

# Function to Send Message
def send_message(event=None):  # Allow event argument for binding
    user_message = user_input.get().strip()
    if user_message:
        # Display user message
        add_message_to_chat(user_message, "You")
        user_input.delete(0, tk.END)  # Clear input field
        
        # Get response from the chatbot
        try:
            response = chat.send_message(user_message)
            bot_message = response.text
        except Exception as e:
            bot_message = "Sorry, there was an error processing your request."
        
        # Display bot message
        add_message_to_chat(bot_message, "Bot")
        user_input.focus()  # Keep focus on input field

# Clear Chat Functionality
def clear_chat(event=None):
    chat_display.config(state="normal")
    chat_display.delete(1.0, tk.END)
    chat_display.config(state="disabled")

# Bind Enter Key to Send Message
user_input.bind("<Return>", send_message)

# Keyboard Shortcut to Clear Chat
root.bind("<Control-l>", clear_chat)

# Send Button
send_button = tk.Button(root, text="Send", font=("Arial", 12), bg="#2980b9", fg="white", command=send_message)
send_button.pack(pady=(0, 10))

# Run the application
root.mainloop()
