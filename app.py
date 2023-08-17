#! /usr/bin/env python3

__version__ = "0.2.0"
__author__ = "Marcelo Garcia"
__license__ = "unlicense"

#entrada de dados
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
print("Operações:\n1-Soma\n2-Subtração\n3-Multiplicação\n4-Divisão")

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
    else:
        print("Opção inválida!")
        continue
    flag = 0
for key, value in oper.items():
    if key == operation:
        print(f"A operação escolhida foi {value}.")

print(f"Você digitou os números: {n1} e {n2}.")
print(f"O resultado da operação é: {res}")

