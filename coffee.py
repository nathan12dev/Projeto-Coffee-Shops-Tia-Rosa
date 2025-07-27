class Cliente:
    def __init__(self, nome, email, senha):   #Aqui é a classe de cliente, onde está seus respectivos objetos: nome, email, senha.
        self.nome = nome                      
        self.email = email
        self.senha = senha

class Pedido:
    def __init__(self, nome, preco, ingredientes):  #Aqui é a classe de pedido, onde está seus respectivos objetos: nome, preco, igredientes
        self.nome = nome
        self.preco = preco
        self.ingredientes = ingredientes
        self.pago = False

def cadastrar_cliente():
    print("\n🔐 Vamos fazer seu cadastro:")  #Função de cadastro dos clientes
    nome = input("Seu nome: ")
    email = input("Seu e-mail: ")
    senha = input("Crie uma senha: ")
    print("\n✅ Cadastro realizado com sucesso!\n")
    return Cliente(nome, email, senha)

def login(cliente):
    print(" Faça login para continuar.\n")
    while True:
        email = input("E-mail: ")             #Função do login dos clientes
        senha = input("Senha: ")
        if email == cliente.email and senha == cliente.senha:
            print(f"\n✅ Login feito com sucesso, bem-vindo {cliente.nome}!\n")
            break
        else:
            print("❌ E-mail ou senha incorretos. Tente novamente.\n")


cardapio = {
    "1": ("Café cremoso simples", 9.00, [       #Aqui é o dicionário de cardápio
        "Meia xícara de leite",
        "4 colheres de café solúvel intenso",
        "Meia lata de creme de leite",
        "4 colheres de chocolate em pó"
    ]),
    "2": ("Café gelado", 8.50, [
        "Café coado",
        "Gelo",
        "Leite a gosto"
    ]),
    "3": ("Mocha gelado", 10.00, [
        "Café forte",
        "Leite gelado",
        "Chocolate em pó",
        "Gelo"
    ]),
    "4": ("Affogato italiano", 11.00, [
        "1 bola de sorvete de creme",
        "1 dose de café espresso quente"
    ]),
    "5": ("Café intenso com chocolate cremoso", 11.50, [
        "Café forte",
        "Chocolate meio amargo derretido",
        "Leite vaporizado"
    ]),
    "6": ("Cappuccino (Promoção)", 7.50, [
        "Café espresso",
        "Leite vaporizado",
        "Espuma de leite",
        "Canela"
    ]),
    "7": ("Cold Brew (Promoção)", 6.90, [
        "Café extraído a frio por 12h",
        "Gelo",
        "Fatia de laranja"
    ])
}

def mostrar_cardapio():                               #Função de mostrar o cárdápio
    print("📋 Cardápio de Cafés")
    for cod, (nome, preco, _) in cardapio.items():
        print(f"{cod} - {nome} - R$ {preco:.2f}")
    print("0 - Sair\n")

def escolher_pedido():                                #Função de Escolher o pedido
    escolha = input("Digite o número do café que deseja ver (ou 0 para sair): ")
    if escolha == "0":
        return None

    if escolha in cardapio:
        nome, preco, ingredientes = cardapio[escolha]
        print(f"\n📝 Ingredientes de {nome}:")
        for item in ingredientes:
            print(f" - {item}")
        confirmar = input("\nDeseja confirmar o pedido? (sim/não): ").lower()
        if confirmar == "sim":
            return Pedido(nome, preco, ingredientes)
        else:
            print("❌ Pedido cancelado.\n")
            return None
    else:
        print("❌ Opção inválida.")
        return None

def realizar_pagamento(pedido):                     #Função de Realizar o pagamento
    print(f"\n✅ Pedido confirmado: {pedido.nome} - R$ {pedido.preco:.2f}")
    print("\n💳 Escolha a forma de pagamento:")
    print("1 - Dinheiro")
    print("2 - Cartão")
    print("3 - PIX")
    forma = input("Forma de pagamento (1/2/3): ")

    if forma in ["1", "2", "3"]:
        pedido.pago = True
        print("\n💲 Pagamento realizado com sucesso. Obrigado pela preferência!\n")
    else:
        print("\n❓ Forma de pagamento não reconhecida. Pedido registrado sem pagamento.\n")

def main():                                         #Função principal do Sistema
    print("=" * 40)
    print("☕ Bem-vindo ao Coffee Shops Tia Rosa ☕")
    print("É um prazer ter você aqui!")
    print("=" * 40)

    cliente = cadastrar_cliente()
    login(cliente)

    pedidos = []

    while True:
        mostrar_cardapio()
        pedido = escolher_pedido()
        if pedido:
            realizar_pagamento(pedido)
            pedidos.append(pedido)
        else:
            continuar = input("Deseja continuar no menu? (sim/não): ").lower()
            if continuar != "sim":
                break

    if pedidos:
        print("\n🧾 Resumo dos pedidos:")
        total = 0
        for i, p in enumerate(pedidos, 1):
            status = "✅ Pago" if p.pago else "⏳ Não pago"
            print(f"{i}. {p.nome} - R$ {p.preco:.2f} | {status}")
            total += p.preco
        print(f"\n💵 Total: R$ {total:.2f}")
    else:
        print("\nVocê não fez nenhum pedido.")

    print("\n☕ Volte sempre ao nosso estabelecimento, Coffee Shops Tia Rosa! ☕")

main()