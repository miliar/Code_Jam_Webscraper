
STATE = ['Draw', 'Game has not completed', 'X won', 'O won']


def evaluate(board):
    end = 0
    row = [None] * 4
    col = [None] * 4
    diag = [None] * 2

    for i in range(4):
        row[i] = {'.': 0, 'T': 0, 'X': 0, 'O': 0}
        col[i] = {'.': 0, 'T': 0, 'X': 0, 'O': 0}
        if i < 2:
            diag[i] = {'.': 0, 'T': 0, 'X': 0, 'O': 0}

    for i in range(4):
        for j in range(4):
            row[i][board[i][j]] += 1
            col[j][board[i][j]] += 1
            if (i == j):
                diag[0][board[i][j]] += 1
            elif i + j == 3:
                diag[1][board[i][j]] += 1

    for i in range(4):
        if i < 2:
            if (diag[i]['T'] + diag[i]['X'] == 4):
                return 2
            elif (diag[i]['T'] + diag[i]['O'] == 4):
                return 3
        if (row[i]['T'] + row[i]['X'] == 4) or (col[i]['T'] + col[i]['X'] == 4) :
            return  2
        elif (row[i]['T'] + row[i]['O'] == 4) or (col[i]['T'] + col[i]['O'] == 4) :
            return 3
    return 0


T = int(raw_input())
for t in range(T):
    board = [raw_input(), raw_input(), raw_input(), raw_input()]
    ignore = raw_input()
    has_space = 1 if '.' in board[0] or  '.' in board[1] or '.' in board[2] or '.' in board[3] else 0
    winner = evaluate(board)
    result = STATE[winner] if winner else STATE[has_space]

    print 'Case #{0}: {1}'.format(t+1, result)
