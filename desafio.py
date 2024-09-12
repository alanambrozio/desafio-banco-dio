menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        deposito = int(input("Digite o valor para depósito: "))
        if deposito >= 0:
            saldo += deposito
            extrato += f"Deposito de R$ {deposito:.2f}\n"
        else:
            print("Valor de depósito inválido.") 
    
    elif opcao == "s":
        saque = int(input("Digite o valor a ser sacado: "))
        if saque > saldo:
            print(f"Valor do saque maior que o saldo, tente um valor menor ou igual à R$ {saldo:.2f}.")
        
        elif saque > 500:
            print("Valor do saque maior que o limite por operação, tente um valor menor ou igual à R$ 500,00")
        
        elif numero_saques >= LIMITE_SAQUES:
            print("Limite de saques diarios atingidos")

        elif saque > 0:
            saldo -= saque
            extrato += f"Saque de R$ {saque:.2f}\n"
            numero_saques += 1 
            
        else:    
            print("Valor de saque invalido.")

    elif opcao == "e":
        print("##############EXTRATO##############")
        print("Sem movimentações na conta" if not extrato else extrato)
        print(f"Saldo na conta é de R$ {saldo:.2f}")
        print("###################################")
    
    elif opcao == "q":
        break
    
    else:
        print("Operação invalida, por favor selecionar novamente a opção desejada.")
