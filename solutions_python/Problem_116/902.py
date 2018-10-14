def ttt(board):
    for row in board:
        winner = win(row)
        if winner:
            return winner

    for i in range(4):
        col = []
        for j in range(4):
            col.append(board[j][i])
        winner = win(col)
        if winner:
            return winner

    diag1 = board[0][0] + board[1][1] + board[2][2] + board[3][3]
    winner = win(diag1)
    if winner:
        return winner

    diag2 = board[0][3] + board[1][2] + board[2][1] + board[3][0]
    winner = win(diag2)
    if winner:
        return winner

    if draw(board):
        return 'Draw'
    else:
        return 'Game has not completed'


def win(line):
    player = None
    prev = 'T'
    for cell in line:
        if (cell == prev or cell == 'T' or prev == 'T') and (cell != '.'):
            if cell != 'T':
                player = cell
                prev = cell
        else:
            return False
    return player + ' won'


def draw(board):
    for row in board:
        for cell in row:
            if cell == '.':
                return False
    return True


def get_board():
    board = []
    board.append(input())
    board.append(input())
    board.append(input())
    board.append(input())
    input()
    return board


cases = int(input())
for i in range(1, cases+1):
    board = get_board()
    print("Case #" + str(i) + ":", ttt(board))

