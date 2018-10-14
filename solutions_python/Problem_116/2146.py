import sys
sys.stdin = open("A-large.in","r")
sys.stdout = open("A-large.out", "w")

X_win = [['X', 'X', 'T', 'X'],
        ['X', 'X', 'X', 'T'],
        ['X', 'T', 'X', 'X'],
        ['T', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X']]
O_win = [['O', 'O', 'T', 'O'],
        ['O', 'O', 'O', 'T'],
        ['O', 'T', 'O', 'O'],
        ['T', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O']]

def checkRow(matrix):
    for i in matrix:
        if i in X_win:
            return -1
        elif i in O_win:
            return 1
    return 0

def checkCol(matrix):
    for i in zip(*matrix):
        if list(i) in X_win:
            return -1
        elif list(i) in O_win:
            return 1
    return 0

def checkDiag(matrix):
    d1 = []
    d2 = []
    for i,row in enumerate(matrix):
        #print i
        d1.append(row[i])
        d2.append(row[3-i])
    return -1 if (d1 in X_win or d2 in X_win) else (1 if (d1 in O_win or d2 in O_win) else 0)

def checkPos(matrix):
    ans = checkRow(matrix)
    if not ans:
        ans = checkCol(matrix)
        if not ans:
            ans = checkDiag(matrix)
            if not ans:
                return "Draw" if sum(['.' in i for i in matrix]) == 0 else "Game has not completed"
    return "O won" if ans == 1 else "X won"

for i in range(input()):
    rows = [list(sys.stdin.readline().strip()) for _ in range(4)]
    #print rows
    print "Case #%d: %s" % (i+1, checkPos(rows))
    extra = sys.stdin.readline()
