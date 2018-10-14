import sys

def fill_here(p, r, c):
    if p[r][c] == '#':
        if r >= len(p) - 1 or c >= len(p[r]) - 1:
            raise ValueError()
        if p[r+1][c] == '#' and p[r+1][c+1] == '#' and p[r][c+1] == '#':
            p[r][c] = p[r+1][c+1] = '/'
            p[r][c+1] =  p[r+1][c] = "\\"
        else:
            raise ValueError()

T = int(sys.stdin.readline())
for t in range(T):
    R, C = map(int, sys.stdin.readline().split())
    paint = [ list(sys.stdin.readline().strip()) for r in range(R) ]

    print "Case #%d:" % (t+1)
    try:
        for r in range(R):
            for c in range(C):
                fill_here(paint, r, c)
        for r in range(R):
            print ''.join(paint[r])
    except ValueError:
        print "Impossible"



