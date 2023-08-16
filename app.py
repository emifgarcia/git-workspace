#! /usr/bin/env python3

__version__ = "0.2.0"
__author__ = "Marcelo Garcia"
__license__ = "unlicense"

#entrada de dados
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
print("Operações:\n1-Soma\n2-Subtração\n3-Multiplicação\n4-Divisão")
operation = int(input("Digite o número da operação: "))

if operation == 1:
    res = n1 + n2
elif operation == 2:
    res = n1 - n2
elif operation == 3:
    res = n1 * n2
elif operation == 4:
    res = n1 / n2
print(f"O resultado da operação é: {res}")