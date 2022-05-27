from http import client
import socket

target_host = "127.0.0.1"
target_port = 9997

#creamos un objeto de socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#enviamos información
client.sendto(b"AAABBBBCCCASDASDASDASDASDAC",(target_host, target_port))

#Recibir la información enviada
data, addr = client.recvfrom(4096)
client.close()