import sys
import re

f = open(sys.argv[1], 'r')

T = int(f.readline())
for t in range(T):
    board = []
    for i in range(4):
        row = list(f.readline().strip())
        board.append(row)
    f.readline()
    
    boardTranspose = zip(*board)
    diag1 = [board[0][0], board[1][1], board[2][2], board[3][3]]
    diag2 = [board[0][3], board[1][2], board[2][1], board[3][0]]
    
    tests = []
    tests.extend(board)
    tests.extend(boardTranspose)
    tests.append(diag1)
    tests.append(diag2)
    
    x_wins = False
    o_wins = False
    draw = True
    
    for row in tests:
        rowString = ''.join(row)
        if re.match('[OT]{4}', rowString):
            o_wins = True
        elif re.match('[XT]{4}', rowString):
            x_wins = True
        if rowString.find('.') > -1:
            draw = False
    
    result = ''
    if x_wins:
        result = 'X won'
    elif o_wins:
        result = 'O won'
    elif draw:
        result = 'Draw'
    else:
        result = 'Game has not completed'
    
    print('Case #%d: %s' % (t + 1, result))

f.close()