# заменить все буквы "х" на "у"

исходная_строка = 'хау ках хорохорится'

новая_строка = ''

for x in исходная_строка:
    if x == 'х':
        новая_строка += 'у'
    else:
        новая_строка += x
print('Ответ на задание 1:')
print(исходная_строка)
print(новая_строка)

# сосчитать произведение чисел, кратных 3 и 5

числа = [1, 3, 5, 15, 25, 45, 75, 100]

произведение = 1

for x in числа:
    if (x // 5 == x / 5) and (x // 3 == x / 3):
        произведение *= x
print('Ответ на задание 2:')
print(произведение)


# Заменить все буквы "х" на "у" в исходной строке без использования дополнительной
import re
строка = 'хау ках хорохорится'

print('Ответ на задание 3:')
print(re.sub(r'х','у',строка))
