# Sistema de Atendimento e Pedidos - Lanchonete
# Trabalho Prático de Algoritmos e Programação
#
# Obs.: o programa usa match-case, então precisa do Python 3.10 ou superior.
# Não uso listas, tuplas, dicionários nem conjuntos, como pede o enunciado.


# ---------------------------------------------------------------
# Funções do cardápio
# ---------------------------------------------------------------

def mostrar_cardapio():
    """Mostra na tela os produtos disponíveis com código e preço."""
    print()
    print("=============== CARDÁPIO ===============")
    print("1 - X-Burger ............ R$ 18,50")
    print("2 - X-Salada ............ R$ 20,00")
    print("3 - Batata Frita ........ R$ 12,00")
    print("4 - Refrigerante ........ R$  6,50")
    print("5 - Suco Natural ........ R$  8,00")
    print("6 - Milkshake ........... R$ 14,90")
    print("0 - Finalizar pedido")
    print("========================================")


def buscar_preco(codigo):
    """Recebe o código digitado e devolve o preço do produto.
    Se o código não existir, devolve 0 (que significa 'inválido',
    já que nenhum produto do cardápio custa zero)."""
    match codigo:
        case "1":
            return 18.50
        case "2":
            return 20.00
        case "3":
            return 12.00
        case "4":
            return 6.50
        case "5":
            return 8.00
        case "6":
            return 14.90
        case _:
            return 0


def buscar_nome_produto(codigo):
    """Recebe o código válido e devolve o nome do produto."""
    match codigo:
        case "1":
            return "X-Burger"
        case "2":
            return "X-Salada"
        case "3":
            return "Batata Frita"
        case "4":
            return "Refrigerante"
        case "5":
            return "Suco Natural"
        case "6":
            return "Milkshake"
        case _:
            return ""


# ---------------------------------------------------------------
# Funções de entrada de dados
# ---------------------------------------------------------------

def pedir_nome():
    """Pede o nome do cliente e só aceita quando não estiver vazio."""
    nome = input("Digite o nome do cliente: ").strip()
    while nome == "":
        print("O nome não pode ficar vazio. Tente novamente.")
        nome = input("Digite o nome do cliente: ").strip()
    return nome


def pedir_quantidade():
    """Pede a quantidade e repete a pergunta até receber um número
    inteiro maior que zero."""
    texto = input("Quantidade desejada: ").strip()
    while not texto.isdigit() or int(texto) <= 0:
        print("Quantidade inválida! Digite um número inteiro maior que zero.")
        texto = input("Quantidade desejada: ").strip()
    return int(texto)


def escolher_pagamento():
    """Mostra as formas de pagamento e repete até o usuário escolher
    uma opção válida. Devolve o nome da forma de pagamento."""
    forma = ""
    while forma == "":
        print()
        print("Escolha a forma de pagamento:")
        print("1 - Dinheiro")
        print("2 - PIX")
        print("3 - Cartão")
        opcao = input("Opção: ").strip()

        match opcao:
            case "1":
                forma = "Dinheiro"
            case "2":
                forma = "PIX"
            case "3":
                forma = "Cartão"
            case _:
                print("Opção de pagamento inválida! Tente novamente.")
    return forma


# ---------------------------------------------------------------
# Funções de cálculo
# ---------------------------------------------------------------

def calcular_subtotal(preco, quantidade):
    """Subtotal = preço do produto vezes a quantidade."""
    return preco * quantidade


def calcular_percentual_desconto(total):
    """Devolve o percentual de desconto de acordo com o valor da compra:
    menos de R$ 50,00 -> 0%
    de R$ 50,00 até R$ 99,99 -> 5%
    R$ 100,00 ou mais -> 10%"""
    if total < 50:
        return 0
    elif total < 100:
        return 5
    else:
        return 10


def calcular_valor_desconto(total, percentual):
    """Transforma o percentual em valor em reais."""
    return total * percentual / 100


# ---------------------------------------------------------------
# Funções de saída de dados
# ---------------------------------------------------------------

def formatar_dinheiro(valor):
    """Deixa o número com 2 casas decimais e vírgula, ex.: 18.5 -> 18,50"""
    texto = f"{valor:.2f}"
    return texto.replace(".", ",")


def mostrar_resumo(nome, valor_original, percentual, valor_desconto,
                   valor_final, pagamento):
    """Imprime o resumo final do atendimento."""
    print()
    print("========== RESUMO DO ATENDIMENTO ==========")
    print(f"Cliente.................: {nome}")
    print(f"Valor original..........: R$ {formatar_dinheiro(valor_original)}")
    print(f"Desconto aplicado.......: {percentual}%")
    print(f"Valor do desconto.......: R$ {formatar_dinheiro(valor_desconto)}")
    print(f"Valor final.............: R$ {formatar_dinheiro(valor_final)}")
    print(f"Forma de pagamento......: {pagamento}")
    print("============================================")
    print(f"Obrigado pela preferência, {nome}! Volte sempre!")


# ---------------------------------------------------------------
# Função principal
# ---------------------------------------------------------------

def atendimento():
    """Controla todo o fluxo do atendimento, do início ao fim."""
    print("Bem-vindo à nossa lanchonete!")
    nome = pedir_nome()

    total = 0.0          # acumula o valor de todos os produtos escolhidos
    continuar = True     # controla o while: vira False quando o cliente finaliza

    while continuar:
        mostrar_cardapio()
        codigo = input("Digite o código do produto: ").strip()

        if codigo == "0":
            # cliente escolheu finalizar, então o laço vai parar
            continuar = False
        else:
            preco = buscar_preco(codigo)

            if preco == 0:
                # código inexistente: avisa e volta ao cardápio sem calcular nada
                print("Código inválido! Escolha um código que esteja no cardápio.")
            else:
                quantidade = pedir_quantidade()
                subtotal = calcular_subtotal(preco, quantidade)
                # round evita erros de arredondamento do float (ex.: 49.9999999)
                total = round(total + subtotal, 2)

                produto = buscar_nome_produto(codigo)
                print()
                print(f"Adicionado: {quantidade}x {produto}")
                print(f"Subtotal deste item: R$ {formatar_dinheiro(subtotal)}")
                print(f"Total até agora: R$ {formatar_dinheiro(total)}")

    # Depois do laço: se não comprou nada, encerra sem pedir pagamento
    if total == 0:
        print()
        print(f"{nome}, nenhum produto foi pedido. Atendimento encerrado.")
    else:
        percentual = calcular_percentual_desconto(total)
        valor_desconto = calcular_valor_desconto(total, percentual)
        valor_final = total - valor_desconto

        print()
        print(f"Valor a pagar: R$ {formatar_dinheiro(valor_final)}")
        pagamento = escolher_pagamento()

        mostrar_resumo(nome, total, percentual, valor_desconto,
                       valor_final, pagamento)


# Início do programa
atendimento()
