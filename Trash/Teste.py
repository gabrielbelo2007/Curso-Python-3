variavel = ['Gabriel', 'Azevedo', 'Belo', 'AJoão']

for valor in variavel:
    if valor.lower().startswith('j'):
        # essa função analisa o primeira caractere de um valor
        break
    print(valor)
    # Lembrando que o python diferencia letra maiúscula de minuscula, por isso a função
    # De deixar a letra minuscula, que poderia ser a de deixar maiscula

else:  # Pode se usar Else com o comando For
    print('Não existe uma palavra que começa com J.')
