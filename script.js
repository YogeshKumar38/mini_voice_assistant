function addMessage(message, sender = 'bot') {
    const box = document.getElementById("chat-box");
    const msg = document.createElement("div");
    msg.className = "bubble" + (sender === 'user' ? ' user' : '');
    msg.textContent = message;
    box.appendChild(msg);
    box.scrollTop = box.scrollHeight;
}

function getCommand() {
    addMessage("🎤 Listening for your command...");
    fetch('/listen')
        .then(response => response.json())
        .then(data => {
            if (data.user) addMessage("You: " + data.user, 'user');
            addMessage("🤖 " + data.reply);
        })
        .catch(error => {
            addMessage("Error: " + error);
        });
}

function sendManualCommand() {
    const input = document.getElementById("manual-input");
    const command = input.value.trim();
    if (!command) return;
    addMessage("You: " + command, 'user');
    input.value = "";
    fetch('/manual', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ command: command })
    })
    .then(response => response.json())
    .then(data => {
        addMessage("🤖 " + data.reply);
    });
}
