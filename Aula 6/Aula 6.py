"""
Variáveis:
Iniciar com letras, pode conter números, separar _, letras minúsculas
"""

nome = 'Gabriel'  # = é um operador de atribuição
idade = 14  #int
altura = 1.68  #float
e_maior = idade > 18  #bool
peso = 50
imc = peso // altura ** 2

# print(nome, type(nome))
print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('Maior de Idade:', e_maior)
print('Idade * Altura:', idade * altura)

print( nome, 'tem', idade, 'anos de idade e seu imc é', imc)
