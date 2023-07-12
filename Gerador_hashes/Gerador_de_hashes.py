import hashlib  

string = input("Digite o texto a ser gerado a hashe: ")

menu = int(input('''  ### ESCOLHA O TIPO DE HASH ###
        1) MD5 
        2) SHA1
        3) SHA256
        4) SHA512
        Digite o número do hash a ser gerado:  '''))

if menu == 1:
    resultado = hashlib.md5(string.encode('utf-8'))
    print('a hash MD5 da String:' , string, 'é: ' , resultado.hexdigest())
elif menu == 2:
    resultado = hashlib.sha1(string.encode('utf-8'))
    print('a hash SHA1 da String:' , string, 'é: ' , resultado.hexdigest())
elif menu == 3:
    resultado = hashlib.sha256(string.encode('utf-8'))
    print('a hash SHA256 da String:' , string, 'é: ' , resultado.hexdigest())
elif menu == 4:
    resultado = hashlib.sha512(string.encode('utf-8'))
    print('a hash SHA512 da String:' , string, 'é: ' , resultado.hexdigest())
else:
    print("Algo de errado não deu certo, escolha uma das opções do menu")



# resultado = hashlib.md5(string.encode('utf-8'))

# print("O hash da String é:", resultado.hexdigest())