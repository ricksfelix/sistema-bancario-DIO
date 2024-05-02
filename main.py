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
        deposito = input('Digite o valor a ser depositado:\nR$')
        if deposito.isnumeric():
            deposito = float(deposito)
            if deposito >= 0:
                msg_deposito = "Realizou um Deposito: R${:.2f}\n".format(deposito)
                print(msg_deposito)
                extrato += msg_deposito
                saldo += deposito
        else: 
            print('Digite um valor Válido!')

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saques = numero_saques >= LIMITE_SAQUES
        excedeu_limite = valor > limite
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print('Você não tem saldo suficiente para realizar o saque!\nValor do saldo: R${:.2f}'.format(saldo))

        elif excedeu_limite:
            print('Você não possui limite para este saque!\nO Limite é de: {:.2f}'.format(limite))

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor >= 0:
            saldo -= valor
            numero_saques += 1
            extrato += f"Saque: R$ {valor:.2f}\n"

        else:
            print('Digite um valor Válido!')


    elif opcao == "e":
        print('========= EXTRATO =========')
        print(extrato)
        print('---------------------------')
        print('Saldo: R${:.2f}'.format(saldo))
        print('===========================')

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")