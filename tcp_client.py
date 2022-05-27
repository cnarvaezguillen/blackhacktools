import socket

target_host = "www.google.com"
target_port = 80

#creamos un objeto socket
client = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

#conectamos con cliente
client.connect((target_host, target_port))

#enviamos datos
client.send(b"GET / HTTPS/1.1\r\nHost: google.com\r\n\r\n")

#Recibiendo los datos enviados
response = client.recv(4096)

print(response.decode())
client.close()