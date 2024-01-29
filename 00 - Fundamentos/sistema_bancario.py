menu = """
----------- MENU ----------- 
|    [d] Depositar          |
|    [s] Sacar              |
|    [e] Extrato            |
|    [q] Sair               |
----------------------------
>>>
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
        valorDeposito = float(input())
        if valorDeposito > 0:
            saldo += valorDeposito
            extrato += f"Depósito: R$ {valorDeposito:.2f}\n"
            print("Depósito realizado. Obrigado por utilizar nossos serviços!")

        else:
            print("Valor inválido para depósito. Tente novamente!")


    elif opcao == "s":
        print("Saque")
        valorSaque = float(input())
        if valorSaque > saldo:
            print("Operação falhou. Você não tem saldo suficiente.")

        elif numero_saques >= LIMITE_SAQUES:
            print("Você atingiu seu limite diário de saque.\nObrigado por utilizar nossos serviços!")

        elif valorSaque > 0 and valorSaque <= 500:
            saldo -= valorSaque
            numero_saques += 1
            extrato += f"Saque: R$ {valorSaque:.2f}\n"
            print("Saque sendo realizado...\nObrigado por utilizar nossos serviços!")

        else:
            print("Você ultrapassou o limite do valor do saque. Tente outro valor abaixo de R$ 500.00")

    elif opcao == "e":
        print("\n----------- EXTRATO -----------")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("-------------------------------")


    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")