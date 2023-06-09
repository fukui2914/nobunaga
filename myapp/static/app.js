function sendMessage(event) {
    event.preventDefault();

    let userInput = document.getElementById('user-input');
    let chatMessages = document.getElementById('chat-messages');

    chatMessages.innerHTML += `<p>あなた: ${userInput.value}</p>`;

    fetch('/message', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            'message': userInput.value
        })
    })
    .then(response => response.json())
    .then(data => {
        chatMessages.innerHTML += `<p>織田信長: ${data.message}</p>`;
    })
    .catch((error) => {
        console.error('Error:', error);
    });

    userInput.value = '';
}


