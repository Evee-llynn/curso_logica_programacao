##copiar 
##soma de dois números:
n1 = int(input('Digite o primeiro número:'))
n2 = int(input('digite o segundo numero:'))
soma = n1 + n2print(f'A soma de  {n1} e {n2} é {soma}.')

## média de duas notas:
nota1 = float(input('Digite a primeira nota:'))
nota2 = float(input('Digite a segunda nota:'))
media = (nota1 + nota2) / 2
print(f'A média é {media:.2f}.')


##trigonometria
import math
angulo = float(input('Digite o ângulo:'))
print(f'Seno: {math.sin(math.radians(angulo)): .2f}, Cosseno: {math.cos(math.radians(angulo)): .2f}, Tangente:{math.tan(math.radians(angulo)): .2f}')


##porção inteira
from math import trunc
n = float(input('Digite um número real: '))
print(f'A porção inteira de {n} é {trunc(n)}.')

##Nome completo
nome = input('Digite seu nome completo: ').strip() 
print(f'Maiúsculas: {nome.upper()}') 
print(f'Minúsculas: {nome.lower()}') 
print(f'Letras ao todo (sem espaços): {len(nome.replace("", ""))}') 
print(f'Primeiro nome: {nome.split() [0]} ({len(nome.split()[0])} letras)')

##Análise de uma frase
frase = input('Digite uma frase: ').upper().strip()
print(f'A letra "A" aparece {frase.count("A")} vezes.') 
print(f'A primeira aparece na posição {frase.find("A") + 1}.')
print(f'A última aparece na posição {frase.rfind("A") + 1}.')

##velocidade
velocidade = float(input('Qual a velocidade do carro?'))
if velocidade > 80:
multa = (velocidade 80) * 7
print(f'Você foi multado! Multa de R${multa:.2f}.')
else:
    print('Tudo certo! Dirija com segurança.')

##par ou ímpar
n = int(input('Digite um número:'))
if n % 2 == 0:
    print('O numero é par')
else:
    print('O numero é impar')
    
##categorias
idade = int(input('Digite a idade do atleta: '))
if idade <=9:
    print('Categoria: MIRIM')
elif idade <=14:
    print('Categoria: Infantil')
elif idade<= 19:
    print('Categoria Junior')
elif idade <= 25:
    print('categoria: SENIOR')
else:
    print('cAtegoria: Master')
    
    
##pagando
preco = float(input('Preço do produto: R$'))
print('''Formas de pagamento:[ 1 ] à vista (dinheiro/cheque) [2] à vista no cartão [3] 2x no cartão [4] 3x ou mais no cartão''')
opcao = int(input('Escolha a opção: '))
if opcao == 1:
    total = preco * 0.9
elif opcao == 2:
    total = preco * 0.95
elif opcao == 3:
    total = preco
    print(f'2x de R${total / 2:.2f}')
elif opcao == 4:
    parcelas = int(input('Número de parcelas: '))
    total = preco * 1.2
    print(f'{parcelas}x de R${total / parcelas:.2f}')
else:
    total = preco
    print('Opção inválida.')
    print(f'Total: R${total:.2f}')
    
##ano nv
from time import sleep
for i in range(10, -1, -1):
    print(i)
    sleep(1)
print('Feliz Ano novo!')

##numeros pares de 1 até 50
for i in range(2, 51, 2):
    print(i, end=' ')
print('Fim')

##cadastro
maior18 = homens = mulheres20 = 0

while True:
idade = int(input('Idade: '))
sexo =
while sexo not in 'MF':
sexo = input('Sexo [M/F]: ').strip().upper()[0]
if idade > 18: maior18 += 1
if sexo == 'M':
homens += 1
if sexo == 'F' and idade < 20:
mulheres20 += 1
continuar =
while continuar not in 'SN':
continuar = input('Quer continuar? [S/N] ').strip().upper() [0]
if continuar == 'N':
    break
print(f'{maior18} pessoas têm mais de 18 anos.')
print(f'{homens} homens foram cadastrados.')
print(f'{mulheres20} mulheres têm menos de 20 anos.')

##par ou impar brincando
from random import randint
vitorias = 0
while True:
    jogador = int(input('Digite um número: ')) computador = randint(0, 10) total = jogador + computador escolha =''
    while escolha not in 'PI':
        escolha = input('Par ou Ímpar? [P/I]: ').strip().upper()[0]
        print(f'Você jogou {jogador} e o computador {computador}. Total de {total}.')
        if escolha == 'P' and total % 2 == 0 or escolha == 'I' and total % 2 == 1:
            print('Você venceu!')
            vitorias += 1
        else:
            print('Você perdeu!')
            break
print(f'Você venceu {vitorias} vezes.')

##parar
soma = 0
while True:
    n = int(input('digite um número(999 para parar):'))
    if n == 999:
        break
    soma += n
print(f'A soma foi{soma}')

##numeros em extenso
extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove''dez', 'onze', 'doze', 
'treze', 'catorze','quinze','dezesseis', 'dezessete', 'dezoito','dezenove', 'vinte')
while True:
    n = int(input('Digite um número entre 0 e 20:'))
    if 0 <= n <= 20:
        break
    print('Tente novamente.')
print(f'Você digitou o número {extenso[n]}.')

##lista sem repetir
numeroS = []
while True:
  n = int(input('Digite um número: '))
  if n not in numeros:
  numeros.append(n)
    print('Número adicionado.')
else:
  print('Número duplicado, não adicionado.')
  continuar = input('Quer continuar? [S/N]: ').strip().upper()
  if continuar == 'N':
    break
numeros.sort()
print(f'Os números digitados foram: {numeros}')


##matriz 3incompleto
matriz[[], [], []]
for i in range(3):
for j in range(3):
n = int(input(f'Digite um numero para [{i}, {j}]: '))
matriz[]


##fute
jogador = {}
partidas = [] jogador['nome'] = input('Nome do jogador: ') jogos = int(input(f'Quantas partidas
{jogador["nome"]} jogou?'))
for i in range(jogos):
partidas.append(int(input(f'Quantos gols na partida {i + 1}? ')))
jogador['gols'] = partidas
jogador['total'] = sum(partidas)
print(jogador)

##funçoes
def maior(*num):
   print(f'Analisando numeros:{num}') 
   print(f'O maior numero é {max(num)}.')
maior(2, 9, 4, 5)