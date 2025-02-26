MENU = """
    ============= MENU =============

    [1] - Depositar
    [2] - Sacar
    [3] - Saldo
    [4] - Novo cliente
    [5] - Criar conta
    [6] - Sair

    ================================
    """

LIMITE_DIARIO = 500
LIMITE_SAQUES = 3
AGENCIA = "0001"
usuarios = []
contas = []

def depositar(saldo, extrato, /):
    valor = float(input("Digite o valor do depósito: "))
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito efetuado com sucesso!")
    else:
        print("Operação não realizada! Procure por um atendente!")
    return saldo, extrato

def sacar(*, saldo, extrato, numero_saques):
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

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:3.2f}")
    print("==========================================")

def criar_cliente(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(usuarios, cpf)
    
    if usuario:
        print("Usuário já cadastrado com esse CPF.")
        return 


    nome = input("Informe o nome completo do cliente: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço do cliente: (logradouro, nro - bairro - cidade/sigla estado)")

    usuarios.append({
        "cpf": cpf,
        "nome": nome,
        "data_nascimento": data_nascimento,
        "endereco": endereco
    })

    print("Usuário cadastrado com sucesso!")

def filtrar_usuario(usuarios, cpf):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(usuarios, cpf)

    if usuario:
        conta = {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
        print(f"Conta cadastrada com sucesso!\nAgência: {conta['agencia']}\nNúmero da Conta: {conta['numero_conta']}\nUsuário: {conta['usuario']['nome']}")
        return conta

    print("Usuário não encontrado!")

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
            exibir_extrato(saldo, extrato=extrato)
        elif opcao == "4":
            criar_cliente(usuarios)
        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
        elif opcao == "6":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()

