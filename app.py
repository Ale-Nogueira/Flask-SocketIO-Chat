from flask import Flask, render_template
from flask_socketio import SocketIO, send
from datetime import datetime

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(data):
    username = data.get('username', 'Anônimo')
    message = data.get('message', '')
    timestamp = datetime.now().strftime('%H:%M')
    formatted_message = f'[{timestamp}] {username}: {message}'
    print(f'Mensagem recebida: {formatted_message}')
    send(formatted_message, broadcast=True)  # Envia a mensagem para todos os clientes conectados

if __name__ == '__main__':
    socketio.run(app, debug=True)