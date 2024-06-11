#sistema bancario2

import textwrap

def menu ():
    menu = """\n
    =============== MENU =================
    [d]\tdepositar
    [s]\tsacar 
    [e]\textrato
    [q]\tNova conta
    [lc]\tlistar contas
    [nu]\tNovo usuário
    [q]\tSair 
    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito:\t£ {valor:.2f}\n"
        print("\n=== Deposito realizado com sucesso! ===")
    else:
        print("\n@@@ operacao falhou! o valor informado é invalido") 
        
    return saldo, extrato   
    
    
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite 
    excedeu_saques = numero_saques > limite_saques
    
    if excedeu_saldo:
        print("\n@@@ operação falhou! você não tem saldo suficiente. @@@")
        
    elif excedeu_limite:
        print("\n@@@ operação falhou, o valor do saque excede o limite.")
    elif excedeu_saques:
        print("\n@@@ operação falhou! numero maximo alcançado.")
        
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\t£ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou, o valor esta invalido,")
        
    return saldo, extrato
def exibir_extrato(saldo, /, *, extrato):
    print("\n========== EXTRATO===========")
    print("não foram realizadas movimentacões." if not extrato else extrato)
    print(f"\nSaldo:\t\t {saldo:.2f}")
    print("==================================")
    
def criar_usuario(usuarios):
    cpf = input("Infome o CPF(somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("\n@@@ Ja existe usuario com esse CPF!")
        return
    nome = input("Informe seu nome completo: ")
    data_nascimento = input(" informe a sua data de nascimento:")
    endereco = input(" informe o endereço (logradouro, nro - bairro - cidade/sigla estado):")
    
    usuarios.append({"nome":nome, "data_nascimento": data_nascimento, "CPF": cpf, "endereco": endereco}) 
    print("==== Úsuario criado com sucesso! ====")
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario ["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input(" informe o CPF do úsuario: ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\n@@@ Úsuario não encontrado, fluxo baixo.")
        
    


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            agencia:\t{conta["agencia"]}
            c/c:\t\t{conta["usuario"]["nome"]}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))
        

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    
    saldo = 0 
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao=menu()
    
        if opcao == "d":
            valor = float(input("informe o valor de deposito:"))
            
            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif opcao == "s":
            valor = float(input("informe o valor do saque:"))
            
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
        
        elif opcao == "e":
            exibir_extrato(saldo, extrato = extrato)
            
        elif opcao == "nu":
            criar_usuario(usuarios)
            
        elif opcao =="nc":
            numero_conta = len(contas) +1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            
            if conta:
                contas.append(conta)
                
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "q":
            break
        else:
            print(" operação invalida, selecione novamnte.")        
        
        
main()        
        