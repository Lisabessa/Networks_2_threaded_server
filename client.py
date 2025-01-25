import socket

def client_connect(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))

    while True:
        msg = input("Введите сообщение: ")
        sock.sendall(msg.encode())

        if msg.lower() == 'exit':
            break

        data = sock.recv(1024).decode()
        print(data)

    sock.close()


client_connect('localhost', 9090)