receita_inicial = float(input("digite o valor da receita:  "))

total_debitos = 0
total_creditos = 0
receita_final = 0

while True:

    operacao= input("digite debito, credito, concluir ou receita final")


    if operacao == "debito":
        valor_debito = float(input("digite o valor: "))
        receita_inicial -= valor_debito
        total_debitos += valor_debito
        print(f"resultado é {valor_debito:.2f} subtraído da receita_inicial")

    elif operacao == "credito":
        valor_credito = float(input("digite o valor: "))
        receita_inicial += valor_credito
        total_creditos += valor_credito
        print(f"resultado é {valor_credito:.2f} adicionado a receita_inicial")

    elif operacao == "receita final":
        receita_final = (receita_inicial - valor_debito + valor_credito)
        print(f"resultado é {receita_final:.2f} valor final")

    elif operacao == "concluir":
        print("\n---Extrato---")
        print(f"receita inicial é {receita_inicial:.2f}")
        print(f"resultado é {total_debitos:.2f}")
        print(f"resultado é {total_creditos:.2f}")
        print(f"resultado é {receita_final:.2f}")

        break

    else:
        print("erro!!! tente novamente. Por favor digite debito, credito, receita final ou concluir" )



