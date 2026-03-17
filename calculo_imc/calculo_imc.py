"""
Calculadora de IMC

Este programa solicita ao usuario sua altura e peso,
calcula o IMC (indice de massa corporal) e exibe a classificação.
"""

def calcula_IMC(peso, altura):
    return peso / (altura ** 2)
    

def classifica_IMC(imc):
    if imc < 18.5:
        print(f"{imc:.2f} é Abaixo do Peso")
    elif imc < 25:
        print(f"{imc:.2f} é Peso Normal")
    elif imc < 30:
        print(f"{imc:.2f} é Sobrepeso")
    elif imc < 35:
        print(f"{imc:.2f} é Obesidade Grau I")
    elif imc < 40:
        print(f"{imc:.2f} é Obesidade Grau II")
    else:
        print(f"{imc:.2f} é Obesidade Grau III")

print("\n--- PROGRAMA DE IMC ---\n")

while True:
    print("1 - Calcular IMC")
    print("0 - Sair\n")

    escolha = int(input("Escolha como prosseguir: "))

    if escolha == 1:
        print("\n--- Você escolheu calcular IMC ---\n")

        peso1 = float(input("Digite o seu peso: "))
        altura1 = float(input("Digite a sua altura: "))

        resultado = calcula_IMC(peso1, altura1)
        print(f"\nO valor do seu IMC é: {resultado:.2f}")

        classifica_IMC(resultado)
        input("Pressione Enter para continuar...\n")
    elif escolha == 0:
        print("\nPrograma encerrado...\n")
        break
    else:
        print("\nEscolha inválida\n")
        input("Pressione Enter para tentar novamente...")