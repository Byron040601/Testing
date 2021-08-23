import socket
import threading

class hilo_cliente(threading.Thread):
    def __init__(self, socket):
        threading.Thread.__init__(self)
        self.socket = socket
    def run(self):
        while True:
            data = self.socket.recv(2048)
            dt = data.decode()
            if(dt == ''):
                continue
            print(dt)

class client():
    def iniciar():
        socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_cliente.connect(('localhost', 2550))
        hilo = hilo_cliente(socket_cliente)
        hilo.start()

        while True:
            data = input('')
            dt = bytes(data, 'UTF-8')
            socket_cliente.send(dt)

client.iniciar()