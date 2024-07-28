import socket # module allows for access to the low-level networking interface
import threading # module provides a way to create and manage multiple threads of execution within a single process

PORT = 5050 # network port for running the server on
SERVER = socket.gethostbyname(socket.gethostname()) # obtains the IP address of local host for the server
ADDRESS = (SERVER, PORT) # variable for binding socket to the ADDRESS
print(f"PORT: {PORT}\nSERVER IP: {SERVER}") # logs port and server IP to console

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # creating a socket using IPv4 and TCP 
server.bind(ADDRESS) # binds socket to ADDRESS

# function handles client and server connection
def handle_client(connnection, address):
    pass

# function handles new connections to the server 
def start():
    server.listen()
    while True:
        connection, address =  server.accept()
        thread = threading.Thread(target=handle_client, args=(connection, address))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

print("[SERVER] server is starting...")
start()