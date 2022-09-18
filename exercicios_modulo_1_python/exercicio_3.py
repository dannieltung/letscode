questions = [
    ('Mora perto da Vítima?'), 
    ('Já trabalhou com a vítima?'), 
    ('Telefonou para a vítima?'),
    ('Esteve no local do crime?'),
    ('Devia para a vítima?')
    ]

answers = []

for each in questions:
    print(each)
    answer = int(input('1-SIM ou 0-NÃO:'))
    if answer != 0 and answer != 1:
        print(each)
        answer = int(input('1-SIM ou 0-NÃO:'))
    answers.append(answer)
question_answer = []

points = 0

for index_question in range(len(questions)):
    if answers[index_question] == 1:
        answer = 'Sim'
        points += 1            
    else:
        answer = 'Não'
    question_answer.append([questions[index_question], answer])
print('------')
print('------')
for each in question_answer:
    print(f'{each[0]} {each[1]}')
if points == 5:
    print('Conclusão: Assasino')
elif points >= 3 and points <= 4:
    print('Conclusão: Cúmplice')
elif points == 2:
    print('Conclusão: Suspeito')
else:
    print('Conclusão: Liberar')