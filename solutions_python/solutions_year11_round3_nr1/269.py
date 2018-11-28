#!/usr/bin/python
import sys

def doit(grid,r,c):
    anything=False
    R = len(grid)
    C = len(grid[0])
    for _r in range(R):
        for _c in range(C):
            if grid[_r][_c]=='#':
                if _c+1 < C and _r+1 < R and \
                  grid[_r+1][_c]=='#' and grid[_r][_c+1]=="#" and grid[_r+1][_c+1]=='#':
                    grid[_r][_c]='/'
                    grid[_r][_c+1]="\\"
                    grid[_r+1][_c] = '\\'
                    grid[_r+1][_c+1] = '/'
                    anything=True
                else:
                    return 'Impossible'
    
    return grid

if __name__ == "__main__":
    f = sys.stdin
    if len(sys.argv) >= 2:
        fn = sys.argv[1]
        if fn != '-':
            f = open(fn)

    t = int(f.readline())
    for _t in xrange(t):
        R,C = map(int,f.readline().split())
        grid = []
        for _r in range(R):
            grid.append(list(f.readline()[:-1]))


        grid = doit(grid,0,0)
   
        if grid=='Impossible':
            print "Case #%d:" % (_t+1)
            print "Impossible"
        else:
            print "Case #%d:" % (_t+1)
            for r in grid:
                s = ""
                for c in r:
                    s+=c
                print s


