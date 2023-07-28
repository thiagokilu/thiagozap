from flask import Flask, render_template
from flask_socketio import SocketIO, send


app = Flask(__name__)
Socketio = SocketIO(app, cors_allowed_origins='*')

#funcionalidade de enviar mensagem
@Socketio.on('message')
def gerenciar_mensagem(mensagem):
    send(mensagem, broadcast=True)

# cria 1 página = 1 rota
@app.route('/')
def homepage():
    return render_template('homepage.html')

#rodar o nosso aplicativo
Socketio.run(app, host='192.168.0.182')