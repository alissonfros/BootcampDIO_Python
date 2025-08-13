from datetime import datetime
data_atual = datetime.now()
data_atual_formatada = data_atual.strftime('%d/%m/%Y %H:%M:%S')
import textwrap


def tela_inicial():
    tela_inicial = """
    ================ MENU PRINCIPAL =================

    Escolha uma das opções abaixo:

    [d] Depositar
    [e] Extrato
    [s] Sacar
    [n] Novo Cliente
    [c] Nova Conta
    [l] Listar Contas
    [q] Sair

    =================================================
    => """
    return input(textwrap.dedent(tela_inicial))


def depositar(saldo, valor, extrato):
    if valor > 0:
        print(f"Depósito realizado com sucesso! Valor depositado: R$ {valor:.2f}")
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação não realizada!!! O valor informado é inválido.")
    return saldo, extrato



def sacar(saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):
    if (valor > saldo): # Verifica se o valor do saque é maior que o saldo disponível em conta
        print("Operação não realizada!!! Você não possui saldo suficiente para esta operação.")

    elif (valor > limite): # Verifica se o valor do saque é maior que o limite da conta
        print("Operação não realizada!!! O valor do saque excede o limite estipulado para saques em sua conta.")

    elif (numero_saques >= LIMITE_SAQUES): # Verifica o limite de saques
        print("Operação não realizada!!! Você já atingiu o limite de saques disponíveis em seu contrato. Favor, contate seu gerente de contas para mais informações.")

    elif valor > 0:
        print(f"Saque realizado com sucesso! Valor sacado: R$ {valor:.2f}")
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Operação não realizada!!!  O valor informado é inválido.")
    return saldo, extrato, numero_saques



def gerar_extrato(saldo, extrato):
    print("\n================== EXTRATO ====================")
    ##print("Emitido em: ", data_atual_formatada)
    print("Não há movimentação realizadas" if not extrato else extrato)
    print(f"\nSaldo Atual: R$ {saldo:.2f}")
    print("=================================================")



def cadastrar_cliente(clientes):
    cpf = input("Digite o CPF (somente números): ")
    
    # Verifica se o cliente já existe
    if any(cliente["cpf"] == cpf for cliente in clientes):
        print("\nCPF já cadastrado! Operação não realizada.")
        return clientes
    
    nome = input("Digite o nome completo: ")
    data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")
    
    print("\nEndereço:")
    logradouro = input("Logradouro: ")
    numero = input("Número: ")
    bairro = input("Bairro: ")
    cidade_uf = input("Cidade/UF: ")
      
    clientes.append({
        "cpf": cpf,
        "nome": nome,
        "data_nascimento": data_nascimento,
        "endereco": {
            "logradouro": logradouro,
            "numero": numero,
            "bairro": bairro,
            "cidade_uf": cidade_uf
        }
    }
    )
    print("\nCliente cadastrado com sucesso!")
    return clientes


def criar_conta(contas, clientes):
    cpf = input("Digite o CPF do titular (somente números): ")
    
    cliente = next((cliente for cliente in clientes if cliente["cpf"] == cpf), None)
    if not cliente:
        print("\nCliente não encontrado! Cadastre o cliente primeiro.")
        return contas
    
    if any(conta["usuario"]["cpf"] == cpf for conta in contas):
        print("\nJá existe uma conta para este CPF!")
        return contas
    
    numero_conta = len(contas) + 1
    contas.append({
        "agencia": "0001",
        "numero_conta": numero_conta,
        "usuario": cliente
    })


    print("\nConta criada com sucesso!")
    return contas


def listar_contas(contas):
    if not contas:
        print("\nNenhuma conta cadastrada!")
        return
    
    print("\n================ CONTAS CADASTRADAS =================")
    for conta in contas:
        print(f"""
        Agência: {conta['agencia']}
        C/C: {conta['numero_conta']}
        Titular: {conta['usuario']['nome']}
        """)
    print("====================================================")


def main():
    saldo = 0
    numero_saques = 0
    LIMITE_SAQUES = 3
    limite = 500
    extrato = ""
    clientes = []
    contas = []


    while True:

        opcao = tela_inicial()

        if opcao == "d":
            valor = float(input("A opção escolhida foi DEPÓSITO. Informe o valor a ser depositado: R$ "))
            saldo, extrato = depositar(saldo, valor, extrato)
            
        elif opcao == "s":
            valor = float(input("A opção escolhida foi SAQUE.Informe o valor a ser sacado: R$ "))
            saldo, extrato, numero_saques = sacar(saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES)
            
        elif opcao == "e":
            gerar_extrato(saldo, extrato)
        elif opcao == "n":
            clientes = cadastrar_cliente(clientes)
        elif opcao == "c":
            contas = criar_conta(contas, clientes)
        elif opcao == "l":
            listar_contas(contas)
        elif opcao == "q":
            print("Obrigado por utilizar nosso sistema bancário!")  
            break
        else:
            print("Operação inválida! Selecione uma opção válida.")


main()