#!/usr/bin/env python
import sys

def solve(coord):
    M = len(coord)
    res = 0
    minx = min( coord[i][n] for i in range(M) for n in [0,2] )
    miny = min( coord[i][n] for i in range(M) for n in [1,3] )
    maxx = max( coord[i][n] for i in range(M) for n in [0,2] )
    maxy = max( coord[i][n] for i in range(M) for n in [1,3] )
    #print minx, miny, maxx, maxy
    for m in range(M):
        coord[m][0] -= minx-1
        coord[m][2] -= minx-1
        coord[m][1] -= miny-1
        coord[m][3] -= miny-1

    B  = [ [False]*(maxy+1) for _ in range(maxx+1) ]
    B2 = [ [False]*(maxy+1) for _ in range(maxx+1) ]
    #print "\n".join(str(s) for s in coord)
    for x1,y1,x2,y2 in coord:
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                B[i][j] = True
    #print "\n".join(str(s) for s in B)
    while True:
        alive = False
        for i in range(1,maxx+1):
            for j in range(1,maxy+1):
                if B[i][j]:
                    B2[i][j] = B[i-1][j] or B[i][j-1]
                else:
                    B2[i][j] = B[i-1][j] and B[i][j-1]

                if B2[i][j]: alive=True

        res += 1
        #print
        #print "\n".join(str(map(int,s)) for s in B)
        if not alive: break
        B = B2
        B2 = [ [False]*(maxy+1) for _ in range(maxx+1) ]

                    
    return res

##############################################
with open(sys.argv[1]) as f:
    T = int(f.readline())
    for case in range(1,T+1):
        N = int(f.readline())
        coord = []
        for n in range(N):
            coord.append( map(int, f.readline().split()) )

        res = solve(coord)
        print "Case #%d: %d" % (case, res)

##############################################

