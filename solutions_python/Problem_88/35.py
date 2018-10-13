T = int(raw_input())

def getsum(g, x1, y1, x2, y2):
    return g[y2][x2]-g[x1-1][y2]-g[x2][y1-1]+g[x1-1][y1-1]

def opt(g, add=lambda a,b: a+b, neg=lambda a: -a):
    t = [[0]*(len(g[0])+1) for i in xrange(len(g)+1)]

    for x in xrange(len(g[0])):
        for y in xrange(len(g)):
            t[y+1][x+1] = add(g[y][x], add(t[y][x+1], add(t[y+1][x], neg(t[y][x]))))

    return t

EPS = 1e-10

def is_blade(x, y, k):
    cx = cy = k-1

    ansx = 0
    ansy = 0
    for tx in xrange(k):
        for ty in xrange(k):
            if (tx==0 and ty == 0) or (tx==0 and ty==(k-1)) or (tx==(k-1) and ty==0) or (tx==k-1 and ty==k-1):
                continue
            ansx += (grid[y+ty][x+tx])*(tx*2-cx)
            ansy += (grid[y+ty][x+tx])*(ty*2-cy)

    #print ansx, ansy
    return ansx == ansy == 0

for case in xrange(1, T+1):
    R, C, D = map(int, raw_input().split())

    grid = []
    for y in xrange(R):
        grid.append(map(int, raw_input()))

    grid_opt = opt(grid)
    #print "\n".join(" ".join(map(str,row)) for row in grid)

    topleft     = [[(0,0)]*C for i in xrange(R)]
    topright    = [[(0,0)]*C for i in xrange(R)]
    bottomleft  = [[(0,0)]*C for i in xrange(R)]
    bottomright = [[(0,0)]*C for i in xrange(R)]

    for x in xrange(C):
        for y in xrange(R):
            topleft[y][x]     = (grid[y][x]*x, grid[y][x]*y)
            topright[y][x]    = (grid[y][x]*(C-1-x), grid[y][x]*y)
            bottomleft[y][x]  = (grid[y][x]*x, grid[y][x]*(R-1-y))
            bottomright[y][x] = (grid[y][x]*(C-1-x), grid[y][x]*(R-1-y))

    #print "\n".join(" ".join(map(str,row)) for row in topleft)

    ans = "IMPOSSIBLE"
    #print is_blade(0,0,4)
    #print is_blade(1,1,5)

    for k in xrange(3,min(R,C)+1):
        for x in xrange(C-k+1):
            if ans == k:
                break
            for y in xrange(R-k+1):
                if is_blade(x, y, k):
                    ans = k
                    break

    print "Case #%d:"%case, ans
