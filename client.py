import socket

HOST = '127.0.0.1'
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("Connected to server. Type commands:")
    while True:
        cmd = input("> ")
        s.sendall(cmd.encode())
        data = s.recv(4096).decode()
        print(data)
        if cmd.strip().upper() == "EXIT":
            break
