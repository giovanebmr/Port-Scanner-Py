# AF_INET para trabalhar com IPV4, SOCK_STREAM para trabalhar com TCP IP
import socket

ip = input('Digite o host ou ip a ser verificado: ')

ports = []
count = 0

while count < 5:
    ports.append(int(input('Digite a porta a ser verificada: ')))
    count += 1

for port in ports:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.05)  # tempo da requisição antes de retornar
    code = client.connect_ex((ip, port))

    if code == 0:
        print(str(port), ' -> Porta aberta')
    else:
        print(str(port), ' -> Porta fechada')

print('Scan finalizado')

