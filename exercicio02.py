"""Escreva um algoritmo para ler as dimensões de um retângulo (base e altura), calcular e escrever a
área do retângulo. """


# Resolução do exercício

Altura = float(input("Digite a altura do retângulo: "))
Base = float(input("Digite a base do retângulo: "))

Area = Altura * Base

print("-"*30)
print("A área do retângulo é {} m²".format(Area))
print("-"*30)