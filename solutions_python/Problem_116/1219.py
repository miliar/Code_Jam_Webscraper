f = open('in.txt')
N = int(f.readline())


def checkSym(sym):
    sym = list(sym)
    if all(k=='T' or k=='X' for k in sym):
        return 'X'
    elif all(k=='T' or k=='O' for k in sym):
        return 'O'
    else:
        return None


def solve(board):
    solns = []

    for i in xrange(4):
        sym = set()
        for j in xrange(4):
            sym.add(board[i][j])
        solns.append(checkSym(sym))

    for j in xrange(4):
        sym = set()
        for i in xrange(4):
            sym.add(board[i][j])
        solns.append(checkSym(sym))

    sym = set([board[0][0], board[1][1], board[2][2], board[3][3]])
    solns.append(checkSym(sym))

    sym = set([board[0][3], board[1][2], board[2][1], board[3][0]])
    solns.append(checkSym(sym))
    #print solns

    if 'X' in solns and 'O' not in solns:
        return 'X won'
    elif 'O' in solns and 'X' not in solns:
        return 'O won'
    else:
        st = ''
        for i in xrange(4):
            st += board[i]
        if '.' in st:
            return 'Game has not completed'
        else:
            return 'Draw'


for i in xrange(N):
    board = []
    for j in xrange(4):
        board.append(f.readline().strip())
    #print board
    print 'Case #'+str(i+1) + ': ' + solve(board)
    f.readline()
