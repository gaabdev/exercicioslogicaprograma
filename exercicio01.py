""" 01.  Escreva um algoritmo que armazene o valor 10 em uma variável A e o valor 20 em uma variável B.
A seguir (utilizando apenas atribuições entre variáveis) troque os seus conteúdos fazendo com que o
valor que está em A passe para B e vice-versa. Ao final, escrever os valores que ficaram armazenados
nas variáveis."""

# Resolução exercício

A = int(input("Digite o Valor de A: "))
B = int(input("Digite o Valor de B: "))

if A == 10:
	valorA = 20
	print(valorA)
else:
	print("Esse valor não é igual a 10!")

if B == 20:
	valorB = 10
	print(valorB)
else:
	print("Esse valor não é igual a 20!")
