
def solve(A):
    for i in xrange(4):
        rX = rO = cX = cO = dX = dO = 0
        for j in xrange(4):
            c1, c2 = A[i][j], A[j][i]
            c3 = A[j][j] if i else A[j][3 - j]
            if c1 == 'X' or c1 == 'T': rX += 1
            if c1 == 'O' or c1 == 'T': rO += 1
            if c2 == 'X' or c2 == 'T': cX += 1
            if c2 == 'O' or c2 == 'T': cO += 1
            if c3 == 'X' or c3 == 'T': dX += 1
            if c3 == 'O' or c3 == 'T': dO += 1
        if rX == 4 or cX == 4 or dX == 4:
            return "X won"
        if rO == 4 or cO == 4 or dO == 4:
            return "O won"
    if any('.' in row for row in A):
        return "Game has not completed"
    return "Draw"

def main(f):
    T = int(f.readline())
    for i in xrange(T):
        A = []
        for j in xrange(4):
            A.append(f.readline().strip())
        f.readline()
        print 'Case #%d:' % (i + 1), solve(A)

if __name__ == '__main__':
    import sys
    main(sys.stdin)
