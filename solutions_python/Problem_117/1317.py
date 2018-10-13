count = int(raw_input())

def check(n,m,board):
    rotated = zip(*board)

    maxrow = [max(board[j]) for j in xrange(n)]
    maxcol = [max(rotated[j]) for j in xrange(m)]

    for j in xrange(n):
        for k in xrange(m):
            cur = board[j][k]
            if cur < maxrow[j] and cur < maxcol[k]:
                return False
    return True

for i in xrange(1,count+1):
    n,m = map(int, raw_input().split())
    board = []
    for _ in xrange(n):
        board.append(map(int, raw_input().split()))

    print "Case #%d:" %i,
    if check(n,m,board):
        print "YES"
    else:
        print "NO"

