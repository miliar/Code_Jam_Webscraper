import sys

def solved(a):
    
    x_count = a.count('X')
    o_count = a.count('O')
    t_count = a.count('T')
    if (x_count == 3 and t_count == 1) or x_count == 4:
        return "X"
    if (o_count == 3 and t_count == 1) or o_count == 4:
        return "O"
    
    if (x_count + o_count + t_count) == 4:
        return "D"

    return "F"

c = int(sys.stdin.readline())
for i in range(c):

    ress = list()
    board = [list(sys.stdin.readline().strip())]
    board.append(list(sys.stdin.readline().strip()))
    board.append(list(sys.stdin.readline().strip()))
    board.append(list(sys.stdin.readline().strip()))

    ress.append(solved(board[0]))
    ress.append(solved(board[1]))
    ress.append(solved(board[2]))
    ress.append(solved(board[3]))

    ress.append(solved([row[0] for row in board]))
    ress.append(solved([row[1] for row in board]))
    ress.append(solved([row[2] for row in board]))
    ress.append(solved([row[3] for row in board]))

    ress.append(solved([board[0][0], board[1][1], board[2][2], board[3][3]]))
    ress.append(solved([board[0][3], board[1][2], board[2][1], board[3][0]]))

    res = "Game has not completed"
    if 'X' in ress:
        res = "X won"
    elif 'O' in ress:
        res = "O won"
    elif 'F' not in ress:
        res = 'Draw'

    sys.stdin.readline()
    print "Case #%d: %s" % (i+1, res)
