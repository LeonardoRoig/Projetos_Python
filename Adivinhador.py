from random import randint
from time import sleep

print('ESTOU PENSANDO EM UM NÚMERO', end='', flush = True)
sleep(1)
print('.', end='', flush = True)
sleep(1)
print('.',end='', flush = True)
sleep(1)
print('.')

num = randint(1,20)
print(num)

sleep(2)
print('Pensei!')

palpite = int(input('Qual o seu palpite?\n'))
tentativas = 1

while True:
    if palpite < num:
        print('Tente um número maior')
    elif palpite > num:
        print('Tente um número menor')
    else:
        print(f'PARABÉNS! TU É O BICHÃO MESMO! CONSEGUIU EM {tentativas} TENTATIVAS')
        break
    
    palpite = int(input('Qual o seu novo palpite?\n'))
    tentativas += 1

    
