# https://code.google.com/codejam/contest/2270488/dashboard#s=p0
import sys

def readline():
    return sys.stdin.readline().rstrip()

# 0 = X won
# 1 = O won
# 2 = Draw
# 3 = Game has not completed
def evaluateBoard(board):
    gameFinished = True
    xWon = False
    oWon = False
    xHcount = [0,0,0,0]
    oHcount = [0,0,0,0]
    xVcount = [0,0,0,0]
    oVcount = [0,0,0,0]
    xDcount = [0, 0]
    oDcount = [0, 0]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'X' or board[i][j] == 'T':
                xHcount[i]+=1
                xVcount[j]+=1
                if i == j:
                    xDcount[0]+=1
                if i+j == 3:
                    xDcount[1]+=1
            if board[i][j] == 'O' or board[i][j] == 'T':
                oHcount[i]+=1
                oVcount[j]+=1
                if i == j:
                    oDcount[0]+=1
                if i+j == 3:
                    oDcount[1]+=1
            if board[i][j] == '.':
                gameFinished = False
    if 4 in xHcount or 4 in xVcount or 4 in xDcount:
        xWon = True
    if 4 in oHcount or 4 in oVcount or 4 in oDcount:
        oWon = True
    if xWon and not oWon:
        return 0
    if not xWon and oWon:
        return 1
    if not gameFinished:
        return 3
    if xWon == oWon:
        return 2
    return -1

t = int(readline())
results = ["X won", "O won", "Draw", "Game has not completed"]
for x in range(t):
    board = []
    for i in range(4):
        line = readline()
        board.append(line)
    readline()
    result = evaluateBoard(board)
    print 'Case #{}: {}'.format(x+1, results[result])


