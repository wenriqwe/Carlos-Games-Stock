# Escolhi um dicionário de dicionários porque o nome do produto é único
# e funciona como chave, permitindo buscar qualquer item diretamente
# pelo nome (ex: estoque["PlayStation 5 slim"]), sem precisar percorrer
# uma lista inteira.
estoque = {
    "PlayStation 5 slim": {"quantidade": 5, "preco": 4500.00},
    "PlayStation 5 pro": {"quantidade": 2, "preco": 7000.00},
    "xbox series s": {"quantidade": 5, "preco": 3250.00},
    "xbox series x": {"quantidade": 1, "preco": 6000.00},
}

while True:
    print("=== CARLOS GAMES ===")
    print("1 - Visualizar Estoque Atual")
    print("2 - Registrar Entrada de Produto")
    print("3 - Registrar Saída de Produto")
    print("4 - Sair do Sistema")
    resposta = input("O que deseja? ")

    if resposta == "1":
        for nome, dados in estoque.items():
            print(
                nome,
                "- Quantidade:",
                dados["quantidade"],
                "- Preço: R$",
                dados["preco"],
            )

    elif resposta == "2":
        nome_produto = input("Qual produto chegou? ")
        quantidade = int(input("Quantos chegaram? "))
        if nome_produto in estoque:
            estoque[nome_produto]["quantidade"] += quantidade
            print("Quantidade atualizada com sucesso!")
        else:
            print("Produto não encontrado.")

    elif resposta == "3":
        nome_produto = input("Qual produto saiu? ")
        quantidade = int(input("Quantas sairam? "))
        if nome_produto in estoque:
            if quantidade <= estoque[nome_produto]["quantidade"]:
                estoque[nome_produto]["quantidade"] -= quantidade
            else:
                print("Etoque insuficiente")
        else:
            print("Produto nao encontrado")

    elif resposta == "4":
        print("Obrigado por usar o sistema CARLOS GAMES. Ate logo!")
        break

    else:
        print("Opcao invalida! Por favor, escolha uma opcao entre 1 e 4.")
