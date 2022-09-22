# Создайте программу для игры в "Крестики-нолики".


import os


def clear():
    return os.system('cls')


def print_board(board):
    for i in range(3):
        print(board[0+i*3], board[1+i*3], board[2+i*3])


def take_input(symbol):
    valid = False
    while not valid:
        n = input('Куда поставим ' + symbol+'? ')
        try:
            n = int(n)
        except:
            print('Некорректный ввод. Это не число.')
            continue
        if n >= 1 and n <= 9:
            if (str(board[n-1]) not in 'XO'):
                board[n-1] = symbol
                valid = True
            else:
                print('Эта клетка занята')
        else:
            print('Некорректный ввод. Введите число от 1 до 9.')


def check_win(board):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                 (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False


board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
clear()
print_board(board)
counter = 0
win = False
while not win:
    clear()
    print_board(board)
    if counter % 2 == 0:
        take_input('X')
    else:
        take_input('O')
    counter += 1
    if counter > 4:
        tmp = check_win(board)
        if tmp:
            clear()
            print(f'Выиграл игрок, играющий за "{tmp}"!')
            print_board(board)
            win = True
            break
    if counter == 9:
        clear()
        print('Ничья!')
        print_board(board)
        break
