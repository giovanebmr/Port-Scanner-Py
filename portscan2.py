import socket

ip = input('Digite o host ou ip a ser verificado: ')

ports = []
count = 0
abertas = []

while count <= 100:
    ports.append( int( count ) )
    count += 1

for port in ports:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.05)  # tempo da requisição antes de retornar
    code = client.connect_ex((ip, port))

    if code == 0:
        print(str(port), ' -> Porta aberta')
        abertas.append( str(port) )
    #else:
        #print(str(port), ' -> Porta fechada')

print('\n________________Scan finalizado_______________________________________________________________' )
print('\n________________________________________Portas abertas________________________________________' )
for port in abertas:
  print(abertas)
