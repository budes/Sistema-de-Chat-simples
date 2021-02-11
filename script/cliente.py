from socket import *

# A porta e o host usados
clienthost = 'localhost' # ou ' '
clientport = 50001

# A instancia do socket
sock = socket(AF_INET, SOCK_STREAM)

# Conecta a esse host por essa portnumber
sock.connect((clienthost, clientport))

while True:
    mensagem = input('Eu: ')
    sock.send(mensagem.encode())

    data = sock.recv(1024)

    print('Ele:', data.decode())

