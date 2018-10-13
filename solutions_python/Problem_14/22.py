import sys

def proc(N, M, A):
    for xa in xrange(N, -1, -1):
        for ya in xrange(M, -1, -1):
            for xb in xrange(N, -1, -1):
                for yb in xrange(M, -1, -1):
                    area = abs(xb*ya-xa*yb)
                    if area == A:
                        return (xa, ya, xb, yb)
    return 

archinp = open(sys.argv[1])
canttests = int(archinp.readline())

for numtest in xrange(1,canttests+1):
    N, M, A = map(int, archinp.readline().split())
    puntos = proc(N, M, A)
    if puntos is None:
        print "Case #%d: IMPOSSIBLE" % numtest
    else:
        xa, ya, xb, yb = puntos
        print "Case #%d: 0 0 %d %d %d %d" % (numtest, xa, ya, xb, yb)
    sys.stdout.flush()
