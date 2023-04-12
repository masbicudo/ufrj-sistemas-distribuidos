import socket

HOST = 'localhost'
PORTA = 5000

sock = socket.socket()
sock.connect((HOST, PORTA))

while True:
    mensagem = input('Echo: ')

    # mensagem vazia é inválida, se deixarmos seguir o programa trava
    if mensagem == "":
        continue

    if mensagem == "fim":
        break

    sock.send(mensagem.encode("utf-8"))

    msg = sock.recv(1024)
    print(str(msg, encoding="utf-8"))

sock.close()
