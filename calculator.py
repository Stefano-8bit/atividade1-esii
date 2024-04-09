import math

num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))

def sum(num1, num2):
    return num1 + num2
print(f"Soma dos numeros {num1} e {num2} Resulta em: ", int(sum(num1, num2)))

# retorna o valor da subtração entre os dois parâmetros
def sub(num1, num2):
    return num1 - num2
print(f"Subtração dos numeros {num1} e {num2} Resulta em: ", int(sub(num1, num2)))


def div(num1, num2):
    if num2 == 0:
        print("❌Não é possivel dividir por zero❌")
        return False
    return num1 / num2
print(f"Divisão dos numeros {num1} e {num2} Resulta em: ", int(div(num1, num2)))

# retorna o valor da multiplicação de dois parâmetros
def mult(num1, num2):
    return num1 * num2
print(f"Multiplicação dos numeros {num1} e {num2} Resulta em: ", int(mult(num1, num2)))

