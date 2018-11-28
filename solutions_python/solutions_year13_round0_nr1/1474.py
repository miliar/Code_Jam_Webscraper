from decimal import *


def check_board(board):
    res = None
    NC = 'Game has not completed'
    p_count = 0
    for i in range(4):
        row = check_set(board[i])
        col = check_set([board[0][i], board[1][i], board[2][i], board[3][i]])
        p_count += board[i].count('.')
        if row != None:
            return row
        if col != None:
            return col
    res = check_set([board[0][0], board[1][1], board[2][2], board[3][3]])
    if res != None:
        return res

    res = check_set([board[0][3], board[1][2], board[2][1], board[3][0]])
    if res != None:
        return res
    if p_count > 0:
        return NC
    return 'Draw'
           
def check_set(set):
    if set.count('X') == 4:
        return 'X won'
    elif set.count('O') == 4:
        return 'O won'
    elif set.count('X') == 3 and set.count('T') == 1:
        return 'X won'
    elif set.count('O') == 3 and set.count('T') == 1:
        return 'O won'
    else:
        return None
    
out = ''  
    
f = open('C:/Users/Thomas/Downloads/A-large.in', 'r')
tests = Decimal(f.readline())
fout = open('C:/Users/Thomas/Downloads/output.out', 'w')
print 'Tests: ' + str(tests)

for test in range(tests):
    board = []
    for i in range(4):
        line = f.readline()
        board.append(line)

    f.readline()
    res = check_board(board)

    ans = 'Case #' + str(test+1) + ': ' + res + '\n'
    print ans
    out = out + ans

f.close()
fout.write(out)
fout.close()
