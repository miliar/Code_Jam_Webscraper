T = int(raw_input())
x_win = lambda x: x == 'X' or x == 'T'
o_win = lambda x: x == 'O' or x == 'T'

def calc(seq):
    if all(o_win(el) for el in seq):
        return 'O'
    if all(x_win(el) for el in seq):
        return 'X'
        
for tt in xrange(T):
    board = [0] * 4
    complete = True
    for row in range(4):
        board[row] = raw_input()
        if '.' in board[row]:
            complete = False
    raw_input()
    res = None
    for row in board:
        res = calc(row) or res
    for col in range(4):
        cool = ''.join(board[i][col] for i in range(4))
        res = calc(cool) or res
    diag = ''.join(board[i][i] for i in range(4))
    res = calc(diag) or res
    diag = ''.join(board[i][3 - i] for i in range(4))
    res = calc(diag) or res
    answer = ''
    if res == 'O':
        answer = "O won"
    elif res == 'X':
        answer = "X won"
    elif complete:
        answer = "Draw"
    else:
        answer = "Game has not completed"
    print "Case #{0}: {1}".format(tt + 1, answer)
