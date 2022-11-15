from random import *
from time import sleep

def Facil():
    print ('Escolheu a dificuldade Facil.')
    print ('Tente escolher o numero que o computador esta pensando')
    num = int(input('Escolha entre 1 e 10: '))
    num_pc = randint(1,10)
    print('=-'*20)
    print(f'O Jogador escolheu o numero -> {num}\n')
    print(f'O Computador escolheu o numero -> {num_pc}')
    print('=-'*20)
    if num == num_pc:
        print ('Jogador Ganhou\n')
    else:
        print ('Jogador Perdeu\n')

def Medio():
    print ('Escolheu a dificuldade Medio.')
    print ('Tente escolher o numero que o computador esta pensando')
    num = int(input('Escolha entre 1 e 50: '))
    num_pc = randint(1,50)
    print('=-'*20)
    print(f'O Jogador escolheu o numero -> {num}\n')
    print(f'O Computador escolheu o numero -> {num_pc}')
    print('=-'*20)
    if num == num_pc:
        print ('Jogador Ganhou\n')
    else:
        print ('Jogador Perdeu\n')

def Dificil():
    print ('Escolheu a dificuldade Dificil.')
    print ('Tente escolher o numero que o computador esta pensando')
    num = int(input('Escolha entre 1 e 100: '))
    num_pc = randint(1,100)
    print('=-'*20)
    print(f'O Jogador escolheu o numero -> {num}\n')
    print(f'O Computador escolheu o numero -> {num_pc}')
    print('=-'*20)
    if num == num_pc:
        print ('Jogador Ganhou\n')
    else:
        print ('Jogador Perdeu\n')

while True:
    print(f'{"Bem vindo ao game de adivinhação":=^30}')
    sleep(1)
    print('''
    Escolha a dificuldade
    [ 0 ] Facil
    [ 1 ] Medio
    [ 2 ] Dificil
    ''')
    sleep(1)
    escolha = int(input('Sua escolha? '))
    sleep(1)

    if escolha == 0:
        Facil()
        continuar = str(input('Quer jogar novamente (S/N)?')).upper()
        if continuar == 'N':
            break
    elif escolha == 1:
        Medio()
        continuar = str(input('Quer jogar novamente (S/N)?')).upper()
        if continuar == 'N':
            break
    elif escolha == 2:
        Dificil()
        continuar = str(input('Quer jogar novamente (S/N)?')).upper()
        if continuar == 'N':
            break
    elif escolha != 0 or 1 or 2:
        print('ERRO... Escolha um numero valido\n')
        sleep(1)

