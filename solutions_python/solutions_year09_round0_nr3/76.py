import sys
f = sys.stdin
N = int(f.readline().strip())
pat = 'welcome to code jam'
for _ in xrange(N):
    ex = f.readline().strip()
    m = len(pat)+1
    n = len(ex)+1
    matrix = [[0 for x in xrange(n)] for y in xrange(m)]
    for x in xrange(n):
        matrix[0][x] = 1
    
    for y in xrange(1,m):
        for x in xrange(1,n):
            matrix[y][x] = (matrix[y][x-1] + (matrix[y-1][x-1] if pat[y-1] == ex[x-1] else 0)) % 10000
#     for line in matrix:
#         print line
    print 'Case #%d: %04d'%((_+1),matrix[-1][-1])

