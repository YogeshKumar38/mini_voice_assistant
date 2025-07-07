🎙 Voice & Text Command Assistant
A Python-based voice command assistant with a clean web interface that supports both voice input and manual text commands. It performs common desktop actions like opening apps, files, and web searches with voice confirmation and an interactive chat UI.

🔧 Features
🎤 Voice & ✍️ Text command support

🧭 Opens installed applications by name

📁 Opens system files by name (via smart file search)

🌐 Searches the web for spoken or typed queries

💬 Chat-style UI with history and confirmation prompts

📂 Optional file selection via file picker

🛑 Supports exit, shutdown, and system-level tasks

📁 Folder Structure
csharp
Copy
Edit
voice_assistant/
│
├── static/
│   ├── style.css       # UI styling
│   ├── script.js       # Client-side logic
│   └── robot.png       # Robot image
│
├── templates/
│   └── index.html      # Frontend interface
│
├── app.py              # Flask backend
└── requirements.txt    # Python dependencies
🚀 How to Run
Clone the repo

bash
Copy
Edit
git clone https://github.com/yourusername/voice_assistant.git
cd voice_assistant
Install requirements

bash
Copy
Edit
pip install -r requirements.txt
Run the app

bash
Copy
Edit
python app.py
Access in browser
Open http://127.0.0.1:5000/

🗣 Sample Commands
open chrome

open file robot.png

search python flask tutorial

who is elon musk

shutdown system

exit

🛠 Tech Stack

Python + Flask

SpeechRecognition

pyttsx3

HTML/CSS/JavaScript

⚠️ Notes
Ensure microphone access is allowed by your OS

For file access, ensure files are present or searchable on your system

Use modern browsers for best compatibility

