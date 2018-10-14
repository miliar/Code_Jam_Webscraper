t = int(raw_input())

def analyze(grid, known, x, y, current):
    if known[y][x] != '?':
        return False
    neighbors = []
    if y > 0: #North
        neighbors.append((x, y-1, grid[y-1][x]))
    if x > 0: #West
        neighbors.append((x-1, y, grid[y][x-1]))
    if x < len(grid[y]) - 1: #East
        neighbors.append((x+1, y, grid[y][x+1]))
    if y < len(grid) - 1: #South
        neighbors.append((x, y+1, grid[y+1][x]))
    if len(neighbors) > 0:
        lowest = min(neighbors, key=lambda i: i[2])
        nx, ny, nv = lowest
    else:
        nx=x
        ny=y
        nv = 99999999999
    if grid[y][x] <= nv: #Sink
        known[y][x] = current
        return True
    elif known[ny][nx] != '?':
        known[y][x] = known[ny][nx]
        return False
    else:
        rv = analyze(grid, known, nx, ny, current)
        known[y][x] = known[ny][nx]
        return rv


for i in xrange(t):
    h, w = map(int, raw_input().split())
    grid = []
    known = []
    for j in xrange(h):
        grid.append(map(int, raw_input().split()))
        known.append(['?'] * w)
    c = "a"
    for y in xrange(h):
        for x in xrange(w):
            rv = analyze(grid, known, x, y, c)
            if rv:
                c = chr(ord(c)+1)
    print "Case #%d:" % (i+1)
    for line in known:
        print " ".join(line)
