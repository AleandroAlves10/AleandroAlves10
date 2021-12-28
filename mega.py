import time
deposito = ('depositar')
print('_____________  Qual o Valor Do Prêmio?  ____________')
time.sleep(1)


mega = float(int(input('Valor da Loteria: ')))
time.sleep(1)
ganhadores = int(input('Número de ganhadores: '))
time.sleep(1)

print('Ok! Esse é o premio para cada jogador: R$ %.2f' %  (mega / ganhadores))
time.sleep(1)

print('Como Você Deseja Resgatar Seu Prêmio?')
time.sleep(1)
print('Processando...')
time.sleep(1)
print('Processando...')
time.sleep(1)

resgate = int(input('Deposito digite 1: ou Presencialmente digite 2:  '))
if resgate == 1:
    print(int(input('Qual o numero da sua conta?:   ')))
    time.sleep(1)
    time.sleep(1)
    print('Processando...')
    time.sleep(1)
    print('Processando...')
    time.sleep(1)
    print('Premio ja esta na sua conta, parabens!')
    
else:
    print('Dirija-se até a lotérica mais proxima!')
    time.sleep(2)
    print('E parabens pelo seu premio')


print('------------------------- Fim do programa! ------------------------')