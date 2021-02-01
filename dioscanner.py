import nmap

scanner = nmap.PortScanner()

print(" Seja bem vindo ao DIOScanner")
print("<---------------------------->")

ip = input("Digite um ip ou host a ser varrido: ")
print("O ip que voce digitou foi: ", ip)
type(ip)

menu = input("""\nEntre com o numero do tipo de Scan que voce deseja fazer:
                    1 -> Scan do tipo SYN
                    2 -> Scan do tipo UDP
                    3 -> Scan do tipo Intenso
                    Numero do Scan: """)

print("Voce escolheu o scan de numero: ", menu)


