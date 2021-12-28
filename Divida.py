                      ##########  DIVIDA RECENTE ################


import time

print('                            ------Programa para controle de dividas----------            ')
time.sleep(3)

valor_divida = int(input('Qual o valor da sua divida?     '))
for i in range(1, 3):
    print('               ................................................')



time.sleep(2)
print(' O valor dela esta em', valor_divida, 'Reais')
time.sleep(1)

for c in range(1,5):
    print('              .................................................')



print('por favor, qual o valor que voce tem disponivel, para amortizar sua divida ? ')
time.sleep(3)

valor_acrecentado = int(input('creditar: '))
for m in range(1, 7):
    print('              ..................................................')
time.sleep(3)

print(valor_acrecentado - valor_divida,'reais é seu valor na conta!')
time.sleep(3)
for i in range(1,9):
    print('              .................................................')
    
if valor_acrecentado >=valor_divida:
    print('Seu saldo esta positivo agora!')
else:
    print('Seu saldo ainda esta negativo!')

time.sleep(7)
for i in range(3):
    print(            '                 -----------------------  FIM  ------------------                       ')
time.sleep(5)
