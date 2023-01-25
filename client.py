import socket
import os
from dotenv import load_dotenv

load_dotenv()

HEADER = 64
PORT = 5050
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
# SET SERVER = YOUR OWN SERVERS IP ADDRESS
SERVER = os.getenv("SERVER_IP")
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

send(input("Message: "))
send(DISCONNECT_MESSAGE)