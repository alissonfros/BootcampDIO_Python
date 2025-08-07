from datetime import date
data_atual = date.today()
data_atual_formatada = data_atual.strftime("%d/%m/%Y %H:%M:%S")


tela_inicial = """
================ MENU PRINCIPAL =================

Escolha uma das opções abaixo:

[d] Depositar
[e] Extrato
[s] Sacar
[q] Sair

=================================================
=> """

saldo = 0
numero_saques = 0
LIMITE_SAQUES = 3
limite = 500
extrato = ""


while True:

    opcao = input(tela_inicial)

    if opcao == "d":
        valor = float(input("A opção escolhida foi DEPÓSITO. Informe o valor a ser depositado: R$ "))

        if valor > 0:
            print(f"Depósito realizado com sucesso! Valor depositado: R$ {valor:.2f}")
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação não realizada!!! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("A opção escolhida foi SAQUE.Informe o valor a ser sacado: R$ "))

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

    elif opcao == "e":
        print("A opção escolhida foi EXTRATO.")
        print("");
        print("");
        print("\n================ EXTRATO ================")
        print("")
        print("Emitido em: ", data_atual_formatada)
        print("");
        print("Não há movimentação realizadas" if not extrato else extrato)
        print("==========================================")
        print(f"\nSaldo Atual: R$ {saldo:.2f}")
        print("")
        print("==========================================")

    elif opcao == "q":
        print("Obrigado por utilizar nosso sistema bancário!")  
        break
    else:
        print("Operação inválida! Selecione uma opção válida.")