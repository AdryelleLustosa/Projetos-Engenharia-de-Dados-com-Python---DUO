# Esse projeto cosiste emcriar um sistema bancario simples em python.
# Para praticar os conceitos de nivel mais básico.
# O projeto tem as funções depositar, sacar e mostrar o extrato.


depositos = []
saques = []
saldo = 0
quant_saque = 0

def depositar(valor):
    global saldo
    depositos.append(valor)
    saldo += valor
    print(f"Seu deposito no valor de R$: {valor_deposito:.2f} foi realizado!")

def sacar (valor):
    global saldo
    global quant_saque

    if saldo < valor: 
        print(f"Você não tem saldo o suficiente para realizar esse saque \n Saldo:{saldo} ")
    else:
        if quant_saque >= 3: 
            print("Você atingiu o limite de 3 saques diarios, tente novamente amanhã.")
        elif valor > 500:
            print("Não é permitido saques maiores que R$ 500,00. Tente novamente")
        elif valor > 0 and valor <= 500:
            
            saques.append(valor)
            saldo -= valor
            quant_saque += 1
            print(f"Seu saque no valor de R$: {valor_saque:.2f} foi realizado!")

def extrato():
    print("\n--- Extrato de Movimentações ---")
    
    if len(depositos) > 0:
        print("\nDepósitos:")
        for i, valor in enumerate(depositos, 1):
            print(f"Depósito {i}: R$ {valor:.2f}")
    else:
        print("\nNenhum depósito realizado.")
    
    if len(saques) > 0:
        print("\nSaques:")
        for i, valor in enumerate(saques, 1):
            print(f"Saque {i}: R$ {valor:.2f}")
    else:
        print("\nNenhum saque realizado.")
    
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("---------------------------------\n")



while True:
    resposta = int(input("""Digite uma opção: 
                         [1] Depositar 
                         [2] Sacar 
                         [3] Extrato 
                         [4] sair
                         """))

    if resposta == 4:
        print("Encerramos seu atendimento.\nObrigada pela preferência")
        break
    elif resposta == 1:
        valor_deposito = float(input("Digite o valor de depósito: "))
        depositar(valor_deposito)
        
    elif resposta == 2:
        valor_saque = float(input("Digite o valor do saque: "))
        sacar(valor_saque)
        
    elif resposta == 3:
        extrato()
    else:
        print("Opção invalida, tente movamente")


