from sys import stdin
nc = int(stdin.readline().strip())

cc=0

def dfs(x,y):
    global grid
    global fill
    global cc
    if fill[y][x] != None:
        return fill[y][x]
    dirs = [ (0,-1), (-1,0), (1,0), (0,1) ]
    bv=100000
    bx,by=None,None
    for dx,dy in dirs:
        nx,ny = x+dx,y+dy
        if nx < 0 or ny < 0 or nx >= len(grid[0]) or ny >= len(grid): continue
        v = grid[y+dy][x+dx]
        if v < bv: bx,by,bv=x+dx,y+dy,v
    if bx is not None and by is not None and grid[by][bx] < grid[y][x]:
        fill[y][x] = dfs(bx,by)
    else:
        fill[y][x] = chr(ord('a')+cc)
        cc += 1
    return fill[y][x]


for c in xrange(1,nc+1):
    cc = 0
    h,w=map(int,stdin.readline().split())
    grid = [ map(int,stdin.readline().split()) for _ in xrange(h) ]
    fill = [ [ None for x in xrange(w) ] for _ in xrange(h) ]
    for y in xrange(h):
        for x in xrange(w):
            dfs(x,y)
            #print
    print "Case #%d:"%c
    for l in fill:
        print " ".join(l)

