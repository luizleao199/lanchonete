# Sistema de Atendimento e Pedidos - Lanchonete

**Estudante:** Luiz Otavio Leão Toledo Dutra Macedo
**Disciplina:** Algoritmos e Programação
**Projeto:** Sistema de Atendimento e Pedidos em Python

## Descrição

Programa em Python que substitui o registro manual de pedidos de uma pequena
lanchonete. O cliente escolhe produtos de um cardápio, informa as quantidades,
recebe desconto conforme o valor da compra, escolhe a forma de pagamento e vê
um resumo completo do atendimento.

## Funcionalidades

- Cadastro do nome do cliente (não aceita nome vazio)
- Cardápio com 6 produtos (código, nome e preço)
- Escolha de vários produtos, com quantidade e subtotal de cada item
- Total da compra acumulado a cada pedido
- Validação de código de produto, quantidade e forma de pagamento
- Desconto automático:
  - abaixo de R$ 50,00: sem desconto
  - de R$ 50,00 até R$ 99,99: 5%
  - R$ 100,00 ou mais: 10%
- Forma de pagamento: Dinheiro, PIX ou Cartão
- Resumo final com cliente, valor original, desconto, valor do desconto,
  valor final e forma de pagamento

## Como executar

1. Instale o Python 3.10 ou superior (o programa usa `match-case`).
2. Baixe o arquivo `lanchonete.py`.
3. No terminal, dentro da pasta do arquivo, rode:

```
python lanchonete.py
```

4. Siga as instruções na tela. Digite `0` no cardápio para finalizar o pedido.
