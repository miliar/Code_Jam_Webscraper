


def solveboard(board):
    complete = True

    # do bfs and mark explored spots
    # CHECK ROWS
    i,j=0,0
    for i in xrange(4):
        #first row
        letter = None
        for j in xrange(4):
            if board[i][j] == '.':
                complete = False
            if letter == None and board[i][j] not in ('.', 'T'):
                letter = board[i][j]
            elif board[i][j] not in (letter, 'T'):
                break # not a solution
            elif board[i][j] in (letter, 'T') and j==3:
                return letter
    # CHECK COLUMNS
    for i in xrange(4):
        #first column
        letter = None
        for j in xrange(4):
            if board[j][i] == '.':
                complete = False
            if letter == None and board[j][i] not in ('.', 'T'):
                letter = board[j][i]
            elif board[j][i] not in (letter, 'T'):
                break # not a solution
            elif board[j][i] in (letter, 'T') and j==3:
                return letter
    # CHECK DIAG
    letter = None
    for i in xrange(4):
        if letter == None and board[i][i] not in ('.', 'T'):
            letter = board[i][i]
        if board[i][i] not in (letter, 'T'):
            break
        elif board[i][i] in (letter, 'T') and i==3:
            return letter
    letter = None
    for i in xrange(4):
        if letter == None and board[i][3-i] not in ('.', 'T'):
            letter = board[i][3-i]
        if board[i][3-i] not in (letter, 'T'):
            break
        elif board[i][3-i] in (letter, 'T') and i==3:
            return letter
    return complete


# MAIN

f = open('t4.in')
out = open('t4out.txt', 'w')
inp = f.read().split('\n')

t = int(inp[0])
numcases = t
n=0

solutions = {'X': 'X won',
             'O': 'O won',
             True: 'Draw',
             False: 'Game has not completed'}

while t>0:
    board = inp[1+(5*n):5+(5*n)]
    #print board
    #print solveboard(board)
    
    ans = 'Case #{0}: {1}'.format(n+1, solutions[solveboard(board)])
    print ans
    out.write(''.join((ans, '\n')))
    
    t-=1
    n+=1
f.close()
out.close()
