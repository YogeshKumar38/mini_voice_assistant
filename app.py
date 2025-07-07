from flask import Flask, render_template, request, jsonify
import speech_recognition as sr
import pyttsx3
import os
import webbrowser
import threading

app = Flask(__name__)
engine = pyttsx3.init()
engine.setProperty('rate', 160)

# App shortcuts
apps = {
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe"
}

# Threaded TTS
def speak(text):
    def run():
        engine.say(text)
        engine.runAndWait()
    thread = threading.Thread(target=run)
    thread.start()
    thread.join()

# Voice command
def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        return "Sorry, I did not catch that."
    except Exception as e:
        return f"Error: {e}"

# 🔍 Search file system for any file name
def find_file(filename, search_path="C:\\"):
    for root, dirs, files in os.walk(search_path):
        if filename.lower() in (f.lower() for f in files):
            return os.path.join(root, filename)
    return None

# 💡 Execute commands
def execute_command(command):
    command = command.lower().strip()

    # Open app
    for name, path in apps.items():
        if name in command:
            speak(f"Opening {name}")
            try:
                os.startfile(path)
                return f"Opening {name}"
            except Exception as e:
                return f"Error opening {name}: {e}"

    # Open file
    if "open file" in command:
        filename = command.replace("open file", "").strip()
        if not filename:
            return "Please say or type the file name."
        speak(f"Searching for {filename}")
        filepath = find_file(filename)
        if filepath:
            try:
                os.startfile(filepath)
                return f"Opened file: {filepath}"
            except Exception as e:
                return f"Error opening file: {e}"
        else:
            return f"File not found: {filename}"

    # Shutdown
    if "shutdown" in command:
        speak("Are you sure you want to shut down?")
        os.system("shutdown /s /t 1")
        return "Shutting down..."

    # Search online
    if "search" in command or "who is" in command:
        query = command.replace("search", "").replace("who is", "").strip()
        speak(f"Searching for {query}")
        webbrowser.open(f"https://www.google.com/search?q={query}")
        return f"Searching for {query}"

    # Exit
    if "exit" in command or "stop" in command:
        speak("Goodbye!")
        return "Assistant exiting..."

    return "Sorry, I can't perform that command."

# Routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/listen")
def listen():
    speak("Listening for your command...")
    command = listen_command()
    result = execute_command(command)
    return jsonify(reply=result)

@app.route("/manual", methods=["POST"])
def manual():
    data = request.get_json()
    command = data.get("command", "")
    speak(f"Executing: {command}")
    result = execute_command(command)
    return jsonify(reply=result)

if __name__ == "__main__":
    app.run(debug=True)
