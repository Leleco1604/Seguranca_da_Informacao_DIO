import os #Importar o módulo ou biblioteca os (Integra os programas e os recursos do s.o)

print("#" * 60)

ip_ou_host = input("Qual é o IP ou Host a ser verificado: ")
#Criando a variavel 
print("- " * 60)

os.system('ping -n 6 {}'.format(ip_ou_host))