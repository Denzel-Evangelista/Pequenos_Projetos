import random
from time import sleep

while True:
    print (''' SUAS OPÇÕES
    [ 0 ] Pedra
    [ 1 ] Papel
    [ 2 ] Tesoura
    ''')

    jogador = int(input('Insira o numero da jogada! '))
    computador = random.choice(['Pedra', 'Papel', 'Tesoura'])
    lista = ('Pedra', 'Papel', 'Tesoura')
    print ('JO')
    sleep(0.5)
    print ('KEN')
    sleep(0.5)
    print ('PO!!!')
    sleep(0.5)
    print ('-=' * 15)
    print (f'Computador jogou {computador}\n')
    print (f'Jogador jogou {lista[jogador]}')
    print ('-=' * 15)

    if computador == 'Pedra':
        if jogador == 0:
            print ('DRAW')
        elif jogador == 1:
            print ('YOU WIN')
        elif jogador == 2:
            print ('YOU LOSE')

    elif computador == 'Papel':
        if jogador == 0:
            print ('YOU LOSE')
        elif jogador == 1:
            print ('DRAW')
        elif jogador == 2:
            print ('YOU WIN')

    elif computador == 'Tesoura':
        if jogador == 0:
            print ('YOU WIN')
        elif jogador == 1:
            print ('YOU LOSE')
        elif jogador == 2:
            print ('DRAW')

    print ('-=' * 15)
    escolha = str(input('Desejar jogar novamente (S/N)? ')).upper()
    if escolha == 'N':
        break