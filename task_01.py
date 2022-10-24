# Задача 1.
# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


my_text = input("Введите текст через пробел:\n")


def invented_words(my_text):
    my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
    return " ".join(my_text)


my_text = invented_words(my_text)
print('Результат удаления слов содержащих "абв":\n', my_text)
