
import random 

#Crie uma variável que contenha todos os caracteres que a senha do usuário pode ter
#Por exemplo: "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

elementos = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
comprimento = int(input("digite o tamanho da senha"))

senha = ""

for i in range(comprimento):
    senha = senha + random.choice(elementos)
print(senha)
#Crie uma variável e peça ao usuário que insira o comprimento da senha
 
#Crie uma variável na qual o programa armazenará a senha gerada
 
#Use um loop e a biblioteca random para selecionar um caractere aleatório da variável de caracteres e adicioná-lo à variável da senha gerada
 
#Exiba a senha resultante no console