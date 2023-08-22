def pedido():
    codigos_e_quantidade = {"CachorroQuente": 4.0, "X-Salada": 4.50, "X-Bacon": 5.00, "TorradaSimples": 2.00, "Refrigerante": 1.50}
    codigo = float(input("Digite o código: "))
    quantidade = int(input("Digite a quantidade: "))
    conta = 0
    
    if codigo == 1:
        conta = codigos_e_quantidade["CachorroQuente"] * quantidade
    elif codigo == 2:
        conta = codigos_e_quantidade["X-Salada"] * quantidade
    elif codigo == 3:
        conta = codigos_e_quantidade["X-Bacon"] * quantidade
    elif codigo == 4:
        conta = codigos_e_quantidade["TorradaSimples"] * quantidade
    else:
        conta = codigos_e_quantidade["Refrigerante"] * quantidade
    
    print(f"Valor total: {conta}")
    
    menu()

def cardapio():
    print("""
          ==================
          
          CÓDIGO
          1
          
          ESPECIFICAÇÃO
          Cachorro Quente
          
          PREÇO
          R$ 4.00
          
          ==================
          
          CÓDIGO
          2
          
          ESPECIFICAÇÃO
          X-Salada
          
          PREÇO
          R$ 4.50
          
          ==================
          
          CÓDIGO
          3
          
          ESPECIFICAÇÃO
          X-Bacon
          
          PREÇO
          R$ 5.00
          
          ==================
          
          CÓDIGO
          4
          
          ESPECIFICAÇÃO
          Torrada simples
          
          PREÇO
          R$ 2.00
          
          ==================
          
          CÓDIGO
          5
          
          ESPECIFICAÇÃO
          Refrigerante
          
          PREÇO
          R$ 1.50
          
          """)
    pedido()

def menu():
    print("""
          Bem vindo
          Escolha uma opção:
          
          0 - Sair
          1 - Cardápio
          2 - Escolher lanche 
          """)
    
    opcao = int(input())

    if opcao == 0:
        quit()
    elif opcao == 1:
        cardapio()
    else: 
        pedido()
menu()