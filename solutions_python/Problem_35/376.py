import sys, pprint

inp = []
grid = []
curbasin = 'a'
basins = {}

def valid(x, y):
    return x >= 0 and y >= 0 and x < len(grid[0]) and y < len(grid)

def basin(x, y):
    d = { }
    # reverse order so that each overwrites earlier if any
    #south
    if valid(x, y+1):
        d[inp[y+1][x]] = (x, y+1)
    #east
    if valid(x+1, y):
        d[inp[y][x+1]] = (x+1, y)
    #west
    if valid(x-1, y):
        d[inp[y][x-1]] = (x-1, y)
    # north
    if valid(x, y-1):
        d[inp[y-1][x]] = (x, y-1)

    d[inp[y][x]] = (y,x)
    
    return d[min(d.keys())]

def resolve(x, y):
    global curbasin
    if y is not None:
        #print 'Resolving: (%d, %d) -> %s'%(x, y, grid[y][x])
        #    return None
        if type(grid[y][x]) == str:
            if grid[y][x] == 'P':
                grid[y][x] = curbasin
                curbasin = chr(ord(curbasin)+1)
            return grid[y][x]
        return resolve( grid[y][x][0], grid[y][x][1] )

def solve(H, W):
    global grid, curbasin
    for i in xrange(H):
        for j in xrange(W):
            x, y = basin( j, i )
            if x == i and y == j:
                #print 'setting', i, j, 'to', curbasin
                grid[i][j] = 'P'
                #curbasin = chr(ord(curbasin)+1)
            else:
                #print 'setting',i, j, 'to',x,y
                grid[i][j] = (x, y)

    for i in xrange(H):
        line = []
        for j in xrange(W):
            line.append(resolve(j, i))
        print ' '.join(line)


T = int(sys.stdin.readline())
for i in xrange(T):
    H, W = map(int, sys.stdin.readline().split())
    inp = []
    grid = []
    curbasin = 'a'
    
    for j in xrange(H):
        inp.append(map(int, sys.stdin.readline().split()))
        grid.append( [ (-1, -1) for _ in range(W) ] )

    print 'Case #%d:'%(i+1)
    solve(H, W)

