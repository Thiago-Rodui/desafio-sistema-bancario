MENU = """
    ============= MENU =============

    [1] - Depositar
    [2] - Sacar
    [3] - Saldo
    [4] - Sair

    ================================
    """

LIMITE_DIARIO = 500
LIMITE_SAQUES = 3

def depositar(saldo, extrato):
    valor = float(input("Digite o valor do depósito: "))
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito efetuado com sucesso!")
    else:
        print("Operação não realizada! Procure por um atendente!")
    return saldo, extrato

def sacar(saldo, extrato, numero_saques):
    valor = float(input("Digite o valor do saque: "))
    excedido_saldo = valor > saldo
    excedido_limite_diario = valor > LIMITE_DIARIO
    excedido_saque = numero_saques >= LIMITE_SAQUES

    if excedido_saldo:
        print("Operação não realizada! Você não tem saldo suficiente")
    elif excedido_limite_diario:
        print("Operação não realizada! Você excedeu o limite diário")
    elif excedido_saque:
        print("Operação não realizada! Você excedeu o limite de saques diários")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque efetuado com sucesso!")
    else:
        print("Operação não realizada! Procure por um atendente!")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:3.2f}")
    print("==========================================")


# Construir o menu principal
def main():
    saldo = 0
    numero_saques = 0
    extrato = ""

    while True:
        opcao = input(MENU)

        if opcao == "1":
            saldo, extrato = depositar(saldo, extrato)
        elif opcao == "2":
            saldo, extrato, numero_saques = sacar(saldo, extrato, numero_saques)
        elif opcao == "3":
            exibir_extrato(saldo, extrato)
        elif opcao == "4":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()

