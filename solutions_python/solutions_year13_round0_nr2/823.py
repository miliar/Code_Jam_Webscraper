import sys

def check(vals, N, M, maxRows, maxCols):
    for i in xrange(N):
        for j in xrange(M):
            if vals[i][j] < maxRows[i] and vals[i][j] < maxCols[j]:
                return False
    return True

T = int(sys.stdin.readline())

for case in xrange(T):
    N, M = sys.stdin.readline().strip().split()

    N = int(N)
    M = int(M)

    vals = [[int(x) for x in sys.stdin.readline().strip().split()] for y in xrange(N)]

    maxRows = [0 for x in xrange(N)]
    maxCols = [0 for x in xrange(M)]

    for i in xrange(N):
        for j in xrange(M):
            if vals[i][j] > maxRows[i]:
                maxRows[i] = vals[i][j]
            if vals[i][j] > maxCols[j]:
                maxCols[j] = vals[i][j]

    if check(vals, N, M, maxRows, maxCols):
        print "Case #%d: %s" % (case+1, "YES")
    else:
        print "Case #%d: %s" % (case+1, "NO")
