#importações de tempo e aleatoridade
from time import sleep
from random import randint
#titulo do jogo
print('Jogo de JOKENPÔ')
sleep(2)

#estrutura de repetição simples
while True:
    
    #pede para o jogador fazer sua escolha
    print("[1] PEDRA\n[2] PAPEL\n[3] TESOURA")
    jogador = int(input('Qual sua escolha? '))
    computador = randint(1, 3)

    #aq começa o temporizador antes do resultado
    print('Jo...')
    sleep(1)

    print('Ken...')
    sleep(1)

    print('PÔ!')
    sleep(0.5)
    
    print(' ')

    #posiveis resultados
    if computador == 1 and jogador == 3: #computador vence escolhendo pedra
        print('Escolhi PEDRA, você PERDEU!')

    elif computador == 2 and jogador == 1: #computador vence escolhendo papel
        print('Escolhi PAPEL, você PERDEU!')

    elif computador == 3 and jogador == 2: #computador vence escolhendo tesoura
        print('Escolhi TESOURA, você PERDEU!')

    elif computador == jogador: #possiveis casos de empate
        if jogador == 1:
            print('Empate! Também escolhi PEDRA!')

        elif jogador == 2:
            print('Empate! Também escolhi PAPEL!')

        else:
            print('Empate! Também escolhi TESOURA!')

    else: #computador perde
        print('EU perdi, você VENCEU!')
    print(' ')

    #pergunta se quer continuação
    continuar = str(input('Quer jogar novamente? (S/N) ')).strip().lower()
    if continuar != 's':
        print(' ')
        print('Jogo finalizado!')
        break
