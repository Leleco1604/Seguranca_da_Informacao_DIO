import random 
import string 


tamanho = int(input("Digite o tamanho da senha que você deseja: "))
#string.ascii_letters = a senha precisa ter letras maiusculas e minusculas
#string.digits =  tem que possuir digitos 
chars = string.ascii_letters + string.digits + '!@#$%&*()-=+,.;:/?'

rnd = random.SystemRandom() 

print(''.join(rnd.choice(chars)for i in range(tamanho)))