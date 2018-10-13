def posgen(n):
    rows = [[(r, i) for i in range(n)] for r in range(n)]
    cols = [[(i, c) for i in range(n)] for c in range(n)]
    diag = [[(i, i) for i in range(n)]]
    diag2 = [[(i, n-i-1) for i in range(n)]]
    return rows + cols + diag + diag2

pos = posgen(4)

def win(board, c):
    for p in pos:
        win = all(map(lambda ch: ch == c or ch == 'T', map(lambda x: board[x[0]][x[1]], p)))
        if win:
            return True
    return False

def boardfull(board):
    for row in board:
        if '.' in row:
            return False
    return True

def matchresult(board):
    xwin = win(board, 'X')
    owin = win(board, 'O')
    isfull = boardfull(board)
    if xwin and owin:
        return 'draw'
    elif xwin:
        return 'X'
    elif owin:
        return 'O'
    elif isfull:
        return 'draw'
    else:
        return 'TBD'


if __name__ == '__main__':
    num = int(raw_input())
    for i in range(num):
        board = []
        for j in range(4):
            row = list(raw_input())
            board.append(row)
        result = matchresult(board)
        if result == 'draw':
            print 'Case #%d: Draw' % (i + 1)
        elif result == 'X':
            print 'Case #%d: X won' % (i + 1)
        elif result == 'O':
            print 'Case #%d: O won' % (i + 1)
        else:
            print 'Case #%d: Game has not completed' % (i + 1)
        raw_input()
