from socket import *

# A porta e o host usados
host = 'localhost' # ou ' '
port = 50001

# A instancia do socket 
sock = socket(AF_INET, SOCK_STREAM)
sock.bind((host, port))

# Ela só lida com 1 conexão por vez
sock.listen(3)

conexao, endereço = sock.accept()

print(endereço, conexao, 'acabou de entrar no chat')

while True:
        
    data = conexao.recv(1024)

    print('Ele:', data.decode())

    mensagem = input('Eu: ')
    conexao.send(mensagem.encode())


    