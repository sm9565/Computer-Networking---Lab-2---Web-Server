# import socket module
from socket import *
import sys  # In order to terminate the program


def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)

    # Prepare a sever socket
    # Fill in start
    host = '127.0.0.1'
    address = (host, port)

    serverSocket.bind(address)
    serverSocket.listen(1)
    # Fill in end

    while True:
        # Establish the connection
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()
        try:
            message = connectionSocket.recv(1024)
            filename = message.split()[1]
            f = open(filename[1:])
            od = f.read()


            # Fill in start
            connectionSocket.send('\nHTTP/1.1 200 OK\n'.encode('utf-8'))
            # Fill in end

            for i in range(0, len(od)):
                connectionSocket.send(od[i].encode())

            connectionSocket.send("\r\n".encode())
            connectionSocket.close()
        except IOError:

            connectionSocket.send('\nHTTP/1.1 404 not found\n'.encode('utf-8'))

            connectionSocket.close()
            # Fill in end

    serverSocket.close()
    sys.exit()  # Terminate the program after sending the corresponding data


if __name__ == "__main__":
    webServer(13331)
