# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def coding(txt):
    count = 1
    res = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            res = res + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        res = res + str(count) + txt[-1]
    return res


def decoding(txt):
    number = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            res = res + txt[i] * int(number)
            number = ''
    return res


with open('task3r.txt', 'r') as file:
    txt = file.read()
print(f'Входные данные из файла:\n{txt}')

with open('task3w.txt', 'w') as data:
    data.write(f'{coding(txt)}\n{decoding(coding(txt))}')

with open('task3w.txt', 'r') as data:
    print(f'Выходные данные из файла:\n{data.read()}')
