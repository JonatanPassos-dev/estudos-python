#meu primeiro programa em python
nome = input("Qual é o seu nome? ")
print("ola,", nome + "!")
print("voce acabou de criar seu primeiro programa.")
print("bem-vindo ao mundo da programação! :)")

# O código acima é um programa simples em Python que solicita
# ao usuário que insira seu nome e, em seguida, exibe uma
# mensagem de saudação personalizada. O programa utiliza a
# função input() para obter a entrada do usuário e a função
# print() para exibir as mensagens na tela. A concatenação
# de strings é feita usando o operador + para combinar a
# saudação com o nome do usuário. O programa também inclui
# mensagens adicionais para dar as boas-vindas ao usuário
# ao mundo da programação.

#Desafio: calcular idade em dias
idade = int(input("quantos anos voce tem? "))

dias = idade * 365
print(f"{nome}, voce viveu aproximadamente {dias} dias!")
print("isso é muito tempo aprendendo coisas novas.")

# O código acima é um programa que calcula a idade de uma
# pessoa em dias. Ele solicita ao usuário que insira seu
# nome e sua idade em anos. Em seguida, o programa multiplica
# a idade por 365 para obter o número aproximado de dias
# vividos. A mensagem final é exibida usando uma f-string
# para formatar a saída, mostrando o nome do usuário e o
# número de dias vividos. O programa também inclui uma
# mensagem adicional para destacar a quantidade de tempo
# que a pessoa passou aprendendo coisas novas.

#if / elif / else
# o programa toma caminhos diferentes dependendo de condições.

nota = int(input("qual foi a sua nota da ultima prova? "))
if nota >= 7:
    print("Então voce foi Aprovado")
elif nota >= 3.1:
    print("voce Passou o valor minimo")
else:
    print("Me desculpe mas... voce foi Reprovado")

# O código acima é um programa que avalia a nota de um aluno
# e determina se ele foi aprovado, está em recuperação ou reprovado.
# O programa solicita ao usuário que insira a nota da última prova
#  e, em seguida, utiliza uma estrutura condicional if/elif/else
#  para verificar a nota. Se esta aprovado, em recuperação ou reprovado.

# Operadores de comparação
# == igual a
# != diferente de
# > maior que
# < menor que
# >= maior ou igual a
# <= menor ou igual a

x = nota
print(x > 5) # True
print(x == 3) # False
print(x != 10) # False
print(x >= 10) # True
print(x < 20) # True

#and / or / not
#combinar varias condições em uma so

tem_habilitação = bool(input("voce tem habilitação? (y/n) "))
if idade >= 18 and tem_habilitação:
    print("pode dirigir")
else:
    print("não pode dirigir")

# O código acima é um programa que verifica se uma pessoa pode dirigir
#  com base em sua idade e se possui habilitação.
#  O programa solicita ao usuário que insira sua idade e se possui habilitação
#  (resposta "y" para sim ou "n" para não).
#  Em seguida, utiliza uma estrutura condicional if/else
#  para verificar se a idade é maior ou igual a 18 e se a pessoa tem habilitação.
#  Se ambas as condições forem verdadeiras printa se não printa.

# Atividade fazer um calculo IMC

PESO = float(input("qual é o seu peso em kg? "))
ALTURA = float(input("qual é a sua altura em metros? "))
IMC = PESO / (ALTURA ** 2)
if IMC >= 18.5 and IMC <= 24.9:
    print("Peso normal")
elif IMC < 18.5:
    print("Abaixo do peso")
elif IMC >= 25 and IMC <= 29.9:
    print("Acima do peso")
else:
    print("Obesidade")

#Operador   Significado     Exemplo Resultado
# +         Adição           5 + 3      8
# -         Subtração        5 - 3      2
# *         Multiplicação    5 * 3      15
# /         Divisão          7 / 2      3.5
# //        Divisão inteira  7 // 2     3
# %         Resto da divisão 7 % 2      1
# **        Potência         2 ** 3     8

