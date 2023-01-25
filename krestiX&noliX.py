board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]  # Пустые клетки, представлены в виде трех пустых списков

winner = None  # Победитель
full = False   # Заполненность поля
moves = []     # Ходы
game = True   # Проверка,можно ли продолжить игру


def display():
    for i in board:
        print("-" * 14)
        for j in i:
            print(" | " + j, end="")
        print(" | ")                # Делаем консольную таблицу с помощью "-" и "|"


def win(player):
    global winner  # Делаем глобальную переменную,без нее игра не заканчиается :)
    b = board   # присваиваем для сокращения кода
    horizontal = b[0][0] == b[0][1] == b[0][2] != ' ' or b[1][0] == b[1][1] == b[1][2] != ' ' or b[2][0] == b[2][1] == b[2][2] != ' '
    vertical = b[0][0] == b[1][0] == b[2][0] != ' ' or b[0][1] == b[1][1] == b[2][1] != ' ' or b[0][2] == b[1][2] == b[2][2] != ' '
    diagonal = b[0][0] == b[1][1] == b[2][2] != ' ' or b[2][0] == b[1][1] == b[0][2] != ' '
    if horizontal or vertical or diagonal:
        winner = player

    for i in board:
        if " " in i:
            full = False
            break
        else:
            full = True
    if full and not winner:
        winner = 'draw'


player = 'X'
while game:
    move = input(f"Игрок ({player}) (Введите позицию для вашего символа) : ")
    if move not in moves:
        moves.append(move)
    else:
        print("Эта позиция занята!")
        continue
    try:
        x, y = int(move[0]), int(move[1])
    except:
        print("Введите правильную позицию!!!")
        continue
    board[2 - y][x] = f"{player}"

    display()
    win(player)
    if winner == player:
        print(f"{player} Победил!")
        game = False
    elif winner == "Ничья":
        print("Это ничья,попробуйте еще!")
        game = False
    if player == 'X':
        player = 'O'
    else:
        player = 'X'

