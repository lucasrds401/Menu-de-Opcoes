#somar, multiplicar, dividir, maior, sair
from time import sleep
from datetime import datetime
l, continuar = '-' * 70, ' '
clear, red, green, yellow, roxo, pink, cyan = '\033[m', '\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m'
print(l)
print(datetime.now().strftime(f'{yellow}%d/%m/%y %H:%M{clear}'))

while continuar not in 'N':
    print(l)
    n1 = int(input(f'Digite o {cyan}1º{clear} valor: '))
    print(l)
    sleep(0.3)
    n2 = int(input(f'Digite o {cyan}2º{clear} valor: '))
    print(l)
    sleep(0.3)
    print(f'''{cyan}MENU DE OPÇÕES{clear} \n
    [1] {red}SOMA{clear}
    [2] {green}MULTIPLICAÇÃO{clear}
    [3] {yellow}DIVISÃO{clear}
    [4] {roxo}MAIOR NÚMERO{clear}
    [5] {pink}SAIR DO PROGRAMA{clear}\n''')
    opção = int(input('Escolha qual opção você prefere: '))
    print(l)
   
    if opção == 1:
        print(f'{cyan}{n1} + {cyan}{n2}{clear} = {cyan}{n1 + n2}')

    elif opção == 2:
        print(f'{cyan}{n1} * {cyan}{n2}{clear} = {cyan}{n1 * n2}')

    elif opção == 3: 
        print(f'{cyan}{n1}{clear} / {cyan}{n2}{clear} = {cyan}{n1/n2}')

    elif opção == 4:
        if n1 > n2:
            print(f'O valor {cyan}{n1}{clear} é maior que o valor {cyan}{n2}')
        elif n1 < n2:
            print(f'O valor {cyan}{n2}{clear} é maior que o valor {cyan}{n1}')
        else:
            print('Os valores são iguais!')
    elif opção == 5:
        print(f'{red}Programa finalizado!')
        continuar = 'S'
    else:
        print('Valor inválido, tente novamente!')
        opção = 5
    print(clear, end ='')
    if opção != 5:
        print(l)
        continuar = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
        while continuar not in 'SN':
            continuar = str(input('Resposta inválida, digite novamente [S/N]: ')).upper().strip()[0]