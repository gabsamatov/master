from random import choice
print('Задайте вопрос мне. Если надоело, напишите "Конец"')
конец = 0
yesornow = ['Да','Нет']
while конец != 1:
    вопрос = input()
    if вопрос =='Конец':
        конец = 1
    else:
        print(choice(yesornow))
else:
    print('Сеанс ответов на вопросы закончен')
