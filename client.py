import socket
import threading
from sys import argv

host,port = argv[1:]
print(host,port)
nickname=input("Choose a nickname: ")

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((host,port))

def receive():
    while True:
        try:
            msg=client.recv(1024).decode("ascii")
            if msg=="NICK":
                client.send(nickname.encode("ascii"))
            else:
                print(msg)
        except:
            print("Brr an error occured...")
            client.close()
            break

def write():
    while True:
        msg=f"\033[92m{nickname}\033[00m: {input('')}"
        client.send(msg.encode("ascii"))

receive_thread=threading.Thread(target=receive)
receive_thread.start()

write_thread=threading.Thread(target=write)
write_thread.start()
