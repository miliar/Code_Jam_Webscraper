from string import maketrans

def colRowDiagSum(list2D):
    colSum =  [sum(x) for x in zip(*list2D)]
    rowSum = map(sum, list2D)
    diagSum = [0, 0]
    n = len(list2D)
    for i in range(n):
        diagSum[0] += list2D[i][i]
        diagSum[1] += list2D[i][n-i-1]
    return colSum + rowSum + diagSum

def convertBoard(board):
    transD = dict(zip('XOT.', [1, 5, 21, 0]))
    list2D = []
    for row in board:
        list2D.append(map(lambda x:transD[x], row))
    return list2D

def getStatus(board):
    list2D = convertBoard(board)
    sums = colRowDiagSum(list2D)
    if 4 in sums or 24 in sums:
        return "X won"
    if 20 in sums or 36 in sums:
        return "O won"
    if 0 in sum(list2D, []):
        return "Game has not completed"
    else:
        return "Draw"


if __name__ == '__main__':
    import sys
    infile = sys.argv[1]
    f = open(infile)
    T = int(f.readline().strip())
    for i in range(T):
        board = []
        for j in range(4):
            ln = board.append(f.readline().strip())
        status = getStatus(board)
        print 'Case #%d: %s'%(i+1, status)
        f.readline()



