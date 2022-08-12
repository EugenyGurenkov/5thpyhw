# Создайте программу для игры в "Крестики-нолики".
    
from random import randint as r
from os import system


def correct_value(player):
    result = input()
    while not result.isdigit() or not (10 > int(result) > 0):
        result = input(f'{player}, можно вводить значения только от 1 до 9: ')
    return int(result)


def player_init():
    player_1 = input('\nВведите имя первого игрока за "X": ')
    player_2 = input('Введите имя второго игрока за "O": ')
    return player_1, player_2


def players_draw(player_1, player_2):
    draw = r(1, 2)
    if draw == 1:
        print(f'\nПо результатам жеребьевки первым ходит {player_1}!')
        return 1
    else:
        print(f'\nПо результатам жеребьевки первым ходит {player_2}!')
        return 2


def draw_field(field):  
    line = '-------------'
    print(line)
    for i in range(3):
        print('|', field[0 + i * 3], '|', field[1 + i * 3],'|', field[2 + i * 3], '|')
    print(line)
    
    
def win_condition(field, turn):
    if field[0] == field[1] == field[2]: return field[0]
    elif field[3] == field[4] == field[5]: return field[3]
    elif field[6] == field[7] == field[8]: return field[6]
    elif field[0] == field[3] == field[6]: return field[0]
    elif field[1] == field[4] == field[7]: return field[1]
    elif field[2] == field[5] == field[8]: return field[2]
    elif field[0] == field[4] == field[8]: return field[0]
    elif field[2] == field[4] == field[6]: return field[2]
    elif all(isinstance(x, str) for x in field): return 'X=O'
    if turn == 1: return 2
    else: return 1


def player_move(field, player, turn):
    draw_field(game_field)
    if turn == 1: print(f'Ходит {player} [X]: ', end = '')
    else: print(f'Ходит {player} [O]: ', end = '')            
    move = correct_value(player)
    while move not in game_field:
        print('Это поле уже занято! Выберете свободное поле: ', end = '')
        move = correct_value(player)
    if turn == 1: field[field.index(move)] = 'X'
    else: field[field.index(move)] = 'O'
            
            
def game(field, player_1, player_2, turn):
    player = None
    while turn == 1 or turn == 2:
        if turn == 1:
            player_move(field, player_1, turn)
            turn = win_condition(game_field, turn) 
            player = player_1    
            system('cls')     
        if turn == 2:
            player_move(field, player_2, turn)
            turn = win_condition(game_field, turn)
            player = player_2
            system('cls')       
    if turn == 'X' or turn == 'O':
        draw_field(game_field)
        print(f'Победили [{turn}]!!! {player} ЧЕМПИОН!!!')
    else:
        draw_field(game_field)
        print('НИЧЬЯ!') 


player_1, player_2 = player_init()
game_field = list(range(1,10))
turn = players_draw(player_1, player_2)
game(game_field, player_1, player_2, turn)
1