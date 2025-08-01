import tkinter as tk
from tkinter import Entry, Label, Button
import webbrowser
import speech_recognition as sr

# --- Main window setup ---
root = tk.Tk()
root.title("AI Assistant")
root.configure(bg='#2c2f33')  # Dark grey background
root.geometry("600x400")      # Window size

# --- Button styling ---
btn_style = {
    "font": ("Arial", 12),
    "bg": "#23272a",             # Dark button
    "fg": "white",               # White text
    "activebackground": "#40444b",
    "activeforeground": "white",
    "width": 25,
    "bd": 1                      
}

# --- Google Search Function ---
def search_google():
    query = entry.get()
    if not query.strip():
        result_label.config(text="Please enter a valid search query.")
        return
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    result_label.config(text="Opened Google search.")

# --- YouTube Search Function ---
def search_youtube():
    query = entry.get()
    if not query.strip():
        result_label.config(text="Please enter a valid search query.")
        return
    url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)
    result_label.config(text="Opened YouTube search.")

# --- Instagram Profile Function ---
def search_instagram():
    username = entry.get().replace("@", "").strip()
    if not username:
        result_label.config(text="Please enter an Instagram username.")
        return
    url = f"https://www.instagram.com/{username}/"
    webbrowser.open(url)
    result_label.config(text=f"Opened Instagram profile: {username}")

# --- Voice Input Function ---
def voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        result_label.config(text="Listening...")
        root.update()  # Update UI immediately
        try:
            audio = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio)
            entry.delete(0, tk.END)
            entry.insert(0, text)
            result_label.config(text="Heard: " + text)
        except sr.WaitTimeoutError:
            result_label.config(text="Listening timed out.")
        except sr.UnknownValueError:
            result_label.config(text="Couldn't understand audio.")
        except sr.RequestError:
            result_label.config(text="Speech recognition service error.")

# --- UI Components ---

# Heading
Label(root, text="AI ASSISTANT", font=("Arial", 18, "bold"), bg="#2c2f33", fg="white").pack(pady=15)

# Subheading
Label(root, text="Enter or speak your command:", font=("Arial", 13), bg="#2c2f33", fg="white").pack()

# Input Field
entry = Entry(root, width=50, font=("Arial", 12), bg="#99aab5", fg="black", insertbackground="black")
entry.pack(pady=10)

# Buttons
Button(root, text="Search on Google", command=search_google, **btn_style).pack(pady=5)
Button(root, text="Search on YouTube", command=search_youtube, **btn_style).pack(pady=5)
Button(root, text="Search on Instagram", command=search_instagram, **btn_style).pack(pady=5)
Button(root, text="Voice Input", command=voice_input, **btn_style).pack(pady=5)

# Output Label (for messages)
result_label = Label(root, text="", font=("Arial", 11), bg="#2c2f33", fg="white", wraplength=500)
result_label.pack(pady=10)

# Start the UI loop
root.mainloop()
