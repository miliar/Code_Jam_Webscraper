from sys import stdin
C = int(stdin.readline().strip())
for c in xrange(C):
    N = int(stdin.readline().strip())
    p = [ map(int,stdin.readline().split()) for _ in xrange(N) ]

    if len(p) < 3:
        best=max( map(lambda x: x[2], p) )

    elif len(p) == 3:
        best=1000000
        for i in xrange(3):
            o = list(set(range(3)) - set([i]))
            best = min(best, max( p[i][2],
                                  (p[o[0]][2] +
                                   p[o[1]][2] +
                                   ((p[o[0]][0] - p[o[1]][0]) ** 2 +
                                    (p[o[0]][1] - p[o[1]][1]) ** 2)**0.5)/2.0))
    print "Case #%d: %f"%(c+1,best)
        
