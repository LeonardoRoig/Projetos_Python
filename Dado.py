import random

def rolaDado(min, max):
    return random.randint(min,max)
    

resposta = 'sim'
while resposta == 'sim':
    num = rolaDado(1,6)
    print(f'Você tirou o número {num} no dado. O seu número é {num}.')
    resposta = input('Você gostaria de rolar o dado mais uma vez? (sim/não)  ').lower()

    while resposta not in ['sim', 'não']:
        resposta = input('Não entendi. Você gostaria de continuar? ').lower()
    
    
    if resposta == 'não':
        print('Obrigado')

            





