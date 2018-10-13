import sys

def run_case():
    n,m = map(int, raw_input().split())
    ans = 'YES'
    board = []
    for i in xrange(n):
        board.append(map(int, raw_input().split()))

    rowmax = [0 for i in xrange(n)]
    colmax = [0 for i in xrange(m)]
    for i in xrange(n):
        for j in xrange(m):
            rowmax[i] = max(board[i][j], rowmax[i])
            colmax[j] = max(board[i][j], colmax[j])
    for i in xrange(n):
        for j in xrange(m):
            if board[i][j] < rowmax[i] and board[i][j] < colmax[j]:
                return 'NO'
    return 'YES'  

for i in xrange(int(raw_input())):
    print >>sys.stderr,(i+1)
    ans = run_case()
    print 'Case #%d:' % (i+1), ans
