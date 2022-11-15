document.addEventListener('DOMContentLoaded', () => {
  const websocketClient = new WebSocket('ws://localhost:12345/')
  
  const messageInput = document.querySelector('[name=message_input]')
  const sendMessageButton = document.querySelector('[name=send_message_button]')
  websocketClient.onopen = () => {
    console.log('Client connected!')

    sendMessageButton.onclick = () => {
      websocketClient.send(messageInput.value)
    }

  }

  websocketClient.onmessage = (message) => {
    console.log(message.data)
  }

}, false)