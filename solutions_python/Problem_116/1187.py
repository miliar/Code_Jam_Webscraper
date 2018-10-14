f = open('A-large.in')
r = open('out.txt', 'w')

import itertools
o_win = [''.join(x) for x in set(itertools.permutations('OOOOT', 4))]
x_win = [''.join(x) for x in set(itertools.permutations('XXXXT', 4))]

def read_board(board):
    for i in range(4):
        if board[i] in o_win:
            return 'O won'
        if board[0][i] + board[1][i] + board[2][i] + board[3][i] in o_win:
            return 'O won'
        if board[i] in x_win:
            return 'X won'
        if board[0][i] + board[1][i] + board[2][i] + board[3][i] in x_win:
            return 'X won'
    if board[0][0] + board[1][1] + board[2][2] + board[3][3] in o_win:
        return 'O won'
    if board[0][3] + board[1][2] + board[2][1] + board[3][0] in o_win:
        return 'O won'
    if board[0][0] + board[1][1] + board[2][2] + board[3][3] in x_win:
        return 'X won'
    if board[0][3] + board[1][2] + board[2][1] + board[3][0] in x_win:
        return 'X won'
    if '.' not in board[0] and '.' not in board[1]\
        and '.' not in board[2] and '.' not in board[3]:
        return 'Draw'
    return 'Game has not completed'
                
n = int(f.readline().strip())
for i in range(n):
    board = []
    for j in range(4):
        board.append(f.readline().strip())
    f.readline()
    print read_board(board)
    r.write('Case #' + str(i+1) + ': ' + read_board(board) + '\n')

f.close()
r.close()
