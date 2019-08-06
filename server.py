# Sample code for testing SERVER CLIENT send msg

import socket
import time

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(),1241))
s.listen(5)

while True:
    # now endpoint look to other endpoint
    clientsocket, address = s.accept()
    print(f'Conection from {address} established.')

    msg = 'You are welcome!'
    msg = f"{len(msg):<{HEADERSIZE}}" + msg

    clientsocket.send(bytes(msg, 'utf-8'))

    while True:
        time.sleep(1)
        msg = f"The time is {time.ctime()}"
        msg = f"{len(msg):<{HEADERSIZE}}" + msg

        print(msg)

        clientsocket.send(bytes(msg, "utf-8"))
