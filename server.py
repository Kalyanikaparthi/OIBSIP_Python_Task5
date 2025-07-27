import socket
import threading

HOST = '127.0.0.1'
PORT = 5000

clients = []

def broadcast(message, sender_socket=None):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message)
            except:
                client.close()
                if client in clients:
                    clients.remove(client)

def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            if not message:
                break
            broadcast(message, client)
        except:
            break
    if client in clients:
        clients.remove(client)
    client.close()

def start_server():
    server.listen()
    print(f"[+] Server running on {HOST}:{PORT}")
    while True:
        client, addr = server.accept()
        print(f"[+] Connected with {addr}")
        clients.append(client)
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

start_server()