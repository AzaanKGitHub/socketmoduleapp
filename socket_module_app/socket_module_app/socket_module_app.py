import socket # module allows for access to the low-level networking interface
import threading # module provides a way to create and manage multiple threads of execution within a single process

HEADER = 64 
PORT = 5050 # network port for running the server on
SERVER = socket.gethostbyname(socket.gethostname()) # obtains the IP address of local host for the server
ADDRESS = (SERVER, PORT) # variable for binding socket to the ADDRESS
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECTED"
print(f"PORT: {PORT}\nSERVER IP: {SERVER}\n------------------------\n") # logs port and server IP to console

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # creating a socket using IPv4 and TCP 
server.bind(ADDRESS) # binds socket to ADDRESS

# function handles client and server connection, this function will run concurrently with each client that is connected 
def handle_client(connection, address):
    print(f"[NEW CONNECTION] {address} connected.")
    connected  = True
    
    while connected:
        message_length = connection.recv(HEADER).decode(FORMAT)
        message_length = int(message_length)
        message = connection.recv(message_length).decode(FORMAT)

        if message == DISCONNECT_MESSAGE:
            connected = False
            
        print(f"[{address}] {message}")
        
    connection.close() 
        

# function handles new connections to the server 
def start():
    server.listen()
    print(f"[SERVER] Listening on {SERVER}")

    while True:
        connection, address =  server.accept()
        thread = threading.Thread(target=handle_client, args=(connection, address))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

print("[SERVER] server is starting...")
start()