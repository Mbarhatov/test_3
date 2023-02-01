def greet():
    print("-------------------")
    print("  Приветсвуем вас  ")
    print("      в игре       ")
    print("  крестики-нолики  ")
    print("-------------------")



# Колличество клеток
board_size = 3

# Игровое поле
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

MODE_HUMAN_VS_HUMAN = '1'
MODE_HUMAN_VS_AI = '2'


def draw_board():
    print('_' * 4 * board_size)
    for i in range(board_size):
        print((' ' * 3 + '|') * 3)
        print('', board[i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], "|")
        print(('_' * 3 + '|') * 3)


def game_step(index, char):
    if (index > 9 or index < 1 or board[index - 1] in ('X', 'O')):
        return False
    board[index - 1] = char
    return True


def check_win(board):
    win = False
    win_combination = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # горизонтальные линии
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # вертикальные линии
        (0, 4, 8), (2, 4, 6)  # диагональные линии
    )
    for pos in win_combination:
        if (board[pos[0]] == board[pos[1]] and board[pos[1]] == board[pos[2]]):
            win = board[pos[0]]

    return win


def computer_step(human, ai):
    '''простой ии для игры с человеком'''

    # наити доступные шаги
    available_steps = [i - 1 for i in board if type(i) == int]

    # успешные шаги в порядке приоритетности
    win_step = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    for char in (ai, human):
        for pos in available_steps:
            # Клонирование игровой доски
            board_ai = board[:]
            board_ai[pos] = char
            if (check_win(board_ai) != False):
                return pos
    # если мы тут, значит не нашли варианты для выигрыша
    for pos in win_step:
        if (pos in available_steps):
            return pos
    return False


def next_player(current_player):
    '''определяем чей следующий ход'''
    if (current_player == 'X'):
        return 'O'
    return 'X'


def start_game(mode):
    current_player = 'X'
    ai_player = 'O'
    step = 1  # номер шага
    draw_board()

    while (step < 10) and (check_win(board) == False):
        index = input(f"Ходит игрок {current_player}. Введите номер поля (0 выход): ")

        if (index == '0'):
            break

        if (game_step(int(index), current_player)):
            print('Удачный ход')
            current_player = next_player(current_player)

            step += 1  # Увеличим номер хода
            if (mode == MODE_HUMAN_VS_AI):
                ai_step = computer_step('X', 'O')
                # Если компьютер нашел куда ходить
                if (type(ai_step) == int):
                    # Ходит компьютер
                    board[ai_step] = ai_player
                    current_player = next_player(current_player)

                    step += 1

            draw_board()
        else:
            print('Неверный номер! Повторите!')
    if (step == 10):
        print('Игра окончина. Ничьия!')
    elif check_win(board) != False:
        print('Выиграл ' + check_win(board))

greet()
mode = 0
while mode not in (MODE_HUMAN_VS_HUMAN, MODE_HUMAN_VS_AI):
    mode = input("Режим игры: \n1 - Человек против человека\n2 - Человек против Компьютера\n выбрать режим игры: ")
start_game(mode)