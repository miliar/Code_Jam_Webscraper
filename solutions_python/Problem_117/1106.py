from sys import stdin


def solve(a, n, m):
    b = [[100 for _ in xrange(m) ] for _ in xrange(n)]
    for i in xrange(n):
        c = max(a[i])
        for j in xrange(m):
            b[i][j] = min(b[i][j], c)
    for j in xrange(m):
        c = max(a[i][j] for i in xrange(n))
        for i in xrange(n):
            b[i][j] = min(b[i][j], c)
    return b == a


t = int(stdin.readline())
for tc in xrange(1, t + 1):
    n,m = (int(x) for x in stdin.readline().split())
    a = [[int(x) for x in stdin.readline().split()] for _ in xrange(n)]

    print "Case #{0}:".format(tc),
    if solve(a,n,m):
        print "YES"
    else:
        print "NO"
