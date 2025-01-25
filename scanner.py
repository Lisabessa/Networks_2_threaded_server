import socket
from tqdm import trange
from concurrent.futures import ThreadPoolExecutor, as_completed

def scan_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((host, port))
    sock.close()
    return port, result == 0


def main():
    host = input("Введите имя хоста или IP-адрес: ")
    with ThreadPoolExecutor(max_workers=256) as executor:
        futures = [executor.submit(scan_port, host, port) for port in trange(1, 65536)]
    
    open_ports = []
    for future in as_completed(futures):
        port, is_open = future.result()
        if is_open:
            open_ports.append(port)
    
    open_ports.sort()
    for port in open_ports:
        print(f"Порт {port} открыт")


main()