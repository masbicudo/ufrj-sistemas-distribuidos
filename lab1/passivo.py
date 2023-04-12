import socket

HOST = ''
PORTA = 5000

sock = socket.socket()
sock.bind((HOST, PORTA))

sock.listen(5)

print("Pronto para receber conexões")

novoSock, endereco = sock.accept()

print(f"Conectado com {endereco}")

while True:
    msg = novoSock.recv(1024)

    if not msg: break
    else: novoSock.send(msg)

novoSock.close()

sock.close()
