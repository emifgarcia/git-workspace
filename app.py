#! /usr/bin/env python3

import time

__version__ = "0.2.0"
__author__ = "Marcelo Garcia"
__license__ = "license"

#entrada de dados
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
time.sleep(1)
print("Operações:\n1-Soma\n2-Subtração\n3-Multiplicação\n4-Divisão\n5-Sair do programa")

oper = {
    1:"soma",
    2:"subtração",
    3:"multiplicação",
    4:"divisão",
}

flag = 1
while flag:
    operation = int(input("Digite o número da operação: "))
    if operation == 1:
        res = n1 + n2
    elif operation == 2:
        res = n1 - n2
    elif operation == 3:
        res = n1 * n2
    elif operation == 4:
        res = n1 / n2
    elif operation == 5: # add na iss#02
        print("Ainda não temos essa opção implementada, digite um número de 1 a 4.") # add na iss#02
        continue # add na iss#02
    else:
        print("Opção inválida!")
        continue
    flag = 0
for key, value in oper.items():
    if key == operation:
        print(f"A operação escolhida foi {value}.")
time.sleep(1)
print(f"Você digitou os números: {n1} e {n2}.")
time.sleep(1)
print(f"O resultado da operação é: {res}")

