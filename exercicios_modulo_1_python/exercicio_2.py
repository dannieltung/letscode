idade = int(input('Idade? '))
while idade < 0 or idade > 150:
    print('Idade deve ser entre 0 e 150 anos.')
    idade = int(input('Idade? '))
print(f'Sua idade: {idade}')
