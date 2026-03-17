"""
Gerenciador de Tarefas

Este programa recebe as tarefas digitadas pelo usuario,
armazena em uma lista, remove tarefas individuais e exibe a lista.
"""

def adicionar_tarefa(tarefas):
    tarefa = input("\nDigite qual tarefa deseja adicionar: ")
    tarefas.append(tarefa)

    print(f"\nA tarefa {tarefa} foi adicionada")
    input("Pressione ENTER para continuar...")

    mostrar_tarefas(tarefas)


def remover_tarefa(tarefas):
    if not tarefas:
        print("\nLista Vazia, Não Há o Que Remover")
        input("Pressione ENTER Para Continuar...\n")
    else:
        tarefa_remover = input("\nDigite qual tarefa deseja remover: ")

        encontrou = False

        for tarefa in tarefas:
            if tarefa_remover == tarefa:
                tarefas.remove(tarefa)

                print(f"\nA tarefa {tarefa} foi removida")
                input("Pressione ENTER para continuar...")

                mostrar_tarefas(tarefas)

                encontrou = True
                break

        if not encontrou:
            print("\nEssa tarefa não está na lista")
            input("Pressione ENTER para continuar...")

            mostrar_tarefas(tarefas)


def mostrar_tarefas(tarefas):
    if not tarefas:
        print("\nA Lista Está Vazia")
    else:
        print("\nEstado da Lista")
        
        for i, tarefa in enumerate(tarefas):
            print(i + 1, "-", tarefa)

    input("Pressione ENTER Para Continuar...\n")

tarefas = []

print("\nPrograma de Lista de Tarefas\n")

while True:
    print("1 - Para Adicionar Tarefas")
    print("2 - Para Remover Tarefas")
    print("3 - Para Listar Tarefas")
    print("0 - Para Sair do Programa")

    escolha = int(input("Escolha Como Deseja Prosseguir: "))

    if escolha == 1:
        adicionar_tarefa(tarefas)
    elif escolha == 2:
        remover_tarefa(tarefas)
    elif escolha == 3:
        mostrar_tarefas(tarefas)
    elif escolha == 0:
        print("\nVocê Saiu do Programa.")
        break
    else:
        print("\nEscolha Inválida, Tente Novamente...")
        input("Pressione ENTER Para Continuar...\n")