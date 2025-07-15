import socket
import os
import shutil

HOST = '127.0.0.1'  # localhost
PORT = 5000

def list_files():
    files = os.listdir('.')
    return '\n'.join(files)

def delete_file(filename):
    try:
        os.remove(filename)
        return f"Deleted {filename}"
    except Exception as e:
        return f"Error: {e}"

def move_file(src, dest):
    try:
        shutil.move(src, dest)
        return f"Moved {src} to {dest}"
    except Exception as e:
        return f"Error: {e}"

def handle_command(cmd):
    parts = cmd.strip().split()
    if not parts:
        return "No command received"
    command = parts[0].upper()
    if command == 'LIST':
        return list_files()
    elif command == 'DELETE' and len(parts) == 2:
        return delete_file(parts[1])
    elif command == 'MOVE' and len(parts) == 3:
        return move_file(parts[1], parts[2])
    elif command == 'EXIT':
        return "Goodbye"
    else:
        return "Invalid command or arguments"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server listening on {HOST}:{PORT}")
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            print(f"Received: {data}")
            response = handle_command(data)
            conn.sendall(response.encode())
            if data.strip().upper() == "EXIT":
                print("Connection closed.")
                break
