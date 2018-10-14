import sys

f = sys.stdin

def valid(x, y, n, m):
    return (x>=0 and y>=0 and x<n and y<m)

def hor(c, x, y, n, m):
    for i in xrange(n):
        if c[i][y] > c[x][y]:
            return False

    return True

def ver(c, x, y, n, m):
    for j in xrange(m):
        if c[x][j] > c[x][y]:
            return False

    return True

def solve(c, n, m):
    for x in xrange(n):
        for y in xrange(m):
            if not (hor(c, x, y, n, m) or ver(c, x, y, n, m)):
                return False
    return True

ncases = int(f.readline().strip())

for case in xrange(ncases):
    line = f.readline().strip().split()
    N = int(line[0])
    M = int(line[1])
    cesped = []
    cesped2 = [[100 for x in xrange(N)] for x in xrange(M)]
    for l in xrange(N):
        li = f.readline().strip()
        li = li.split(' ')
        cesped.append(map(lambda x: int(x), li))
    s = solve(cesped, N, M)
    if s : 
        s="YES" 
    else: 
        s="NO"
    print "Case #"+str(case+1) + ": " + s

