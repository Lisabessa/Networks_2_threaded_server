import socket
from threading import Thread

def handle_client(conn, addr):
    print(f"Подключен клиент {addr}")
    
    while True:
        data = conn.recv(1024)
        
        if not data:
            break
        
        print(f'[{addr[0]}:{addr[1]}]: {data.decode()}')
        conn.sendall(data)
    
    conn.close()
    print(f"Клиент {addr} отключился")


def run_echo_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', 9090))
    sock.listen(5)

    while True:
        conn, addr = sock.accept()
        Thread(target=handle_client, args=(conn, addr), daemon=True).start()


run_echo_server()