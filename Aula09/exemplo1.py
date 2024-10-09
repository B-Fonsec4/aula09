# try:
#     n = int(input('Informe um numero: '))
# except:
#     print('erro')


try:
    n = input('Informe uma letra: ')[0]
except (ValueError, KeyboardInterrupt) as e:
    print(f'Erro: {e}')
else:
    print(f'Você informou variavel {n}')

    
# try:
#     txt = input('informe um nome: ')[0]
# except IndexError as e:
#     print(f' {e} Precisa digitar algo')
# else:
#     print('Acertou!!!!')
# finally:
#     print('sempre executado')



 