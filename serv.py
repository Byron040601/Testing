import socket
import threading

class hilo_servidor(threading.Thread):
    def __init__(self, conexion, direccion, sockets):
        threading.Thread.__init__(self)
        self.conexion = conexion
        self.direccion = direccion
        self.sockets = sockets

    def run(self):
        print("\nNueva conexion: ", self.direccion[0])
        for sock in self.sockets:
            try:
                data = "\n" + self.direccion[0] + "Conectado"
                b = bytes(data, 'UTF-8')
                sock.send(b)
            except Exception as identifier:
                continue

        while True:
            data = self.conexion.recv(2048)
            dt = data.decode()
            if(dt == ''):
                continue

            print(self.direccion[0], " > ", dt)

class servidor():
    def inciar():
        clients_sockets = []
        hilos = []
        socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_server.bind(('localhost', 2550))
        socket_server.listen(3)
        print("Aguardando por una conexion.")

        while True:
            connection_socket, direction = socket_server.accept()
            hilo = hilo_servidor(connection_socket, direction, clients_sockets)
            hilo.start()
            hilos.append(hilo)
            clients_sockets.append(connection_socket)

servidor.inciar()