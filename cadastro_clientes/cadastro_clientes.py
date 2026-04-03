"""
Programa de cadastro de clientes

Este programa recebe informações de clientes,
armazena em uma lista de clientes, e exibe essa lista para consulta,
quando necessario pode remover clientes da lista.
"""

def adicionar_cliente(clientes):
    while True:
        nome = input("\nDigite o nome: ")
        
        if nome.strip() == "":
            print("\nNome inválido")
            input("Pressione ENTER para tentar novamente...")
            continue

        telefone = (input("Digite o número de telefone: "))

        if not telefone.isdigit() or len(telefone) < 10 or len(telefone) > 11:
            print("Número inválido")
            input("Pressione ENTER para tentar novamente...")
            continue

        email = input("Digite o email: ")

        if "@" not in email or "." not in email:
            print("Email inválido")
            input("Pressione ENTER para tentar novamente...")
            continue

        partes_email = email.split("@")

        if partes_email[0] == "" or partes_email[1] == "":
            print("Email inválido")
            input("Pressione ENTER para tentar novamente...")
            continue

        cliente = {
            "nome": nome,
            "telefone": telefone,
            "email": email
        }

        clientes.append(cliente)
        break
    

def remover_cliente(clientes):
    if not clientes:
        print("\nSem clientes para remover")
    else:
        nome_remover = input("\nDigite qual cliente deseja remover: ")

        encontrado = False

        for i, cliente in enumerate(clientes):
            if cliente['nome'] == nome_remover:
                clientes.pop(i)

                print(f"\nO cliente {cliente['nome']} foi removido")
                encontrado = True
                break

        if not encontrado:
            print("\nEsse nome não foi encontrado")
    
    input("Pressione ENTER para continuar...")

def mostrar_clientes(clientes):
    if not clientes:
        print("\nNenhum cliente cadastrado")
    else:
        print("\nClientes cadastrados:\n")

        for i, cliente in enumerate(clientes):
            print(f"{i + 1} - Nome: {cliente['nome']} - Telefone: {cliente['telefone']} - Email: {cliente['email']}\n")

    input("Pressione ENTER para continuar...")

clientes = []

print("Programa simples de cadastro de clientes\n")

while True:
    print("\n1 - Adicionar cliente")
    print("2 - Remover cliente")
    print("3 - Listar todos os clientes")
    print("0 - Sair do programa")

    escolha = int(input("Escolha como prosseguir: "))

    if escolha == 1:
        adicionar_cliente(clientes)
    elif escolha == 2:
        remover_cliente(clientes)
    elif escolha == 3:
        mostrar_clientes(clientes)
    elif escolha == 0:
        print("\nVocê saiu do programa")
        break
    else:
        print("Escolha inválida")
        input("Pressione ENTER para tentar novamente...")