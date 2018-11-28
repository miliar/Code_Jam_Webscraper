T = int(raw_input())


def fill_horizontal(i, j):
    global R, C, grid
    c = j-1
    w = 1
    while 0 <= c and c < C and (grid[i][c] == "?" or grid[i][c] == grid[i][j]):
        grid[i][c] = grid[i][j]
        w += 1
        c -= 1

    c = j+1
    while 0 <= c and c < C and (grid[i][c] == "?" or grid[i][c] == grid[i][j]):
        grid[i][c] = grid[i][j]
        w += 1
        c += 1

    return w

def fill_vert(i, j):
    global R, C, grid, widths
    w = widths[grid[i][j]]
    target = ["?"]*w
    c = i-1
    while 0 <= c and c < R and grid[c][j:j+w] == target:
        for l in range(j, j+w):
            grid[c][l] = grid[i][j]
        c -= 1

    c = i+1
    while 0 <= c and c < R and grid[c][j:j+w] == target:
        for l in range(j, j+w):
            grid[c][l] = grid[i][j]
        c += 1

for a in xrange(T):
    R, C = map(int, raw_input().split())
    grid = []
    for b in range(R):
        grid.append(list(raw_input()))
    widths = dict()
    prev = ""
    for i in xrange(R):
        for j in xrange(C):
            if grid[i][j] != "?" and grid[i][j] != prev:
                width = fill_horizontal(i, j)
                prev = grid[i][j]
                widths[prev] = width
    prev = ""
    for i in xrange(R):
        for j in xrange(C):
            if grid[i][j] != "?" and grid[i][j] != prev:
                fill_vert(i, j)
                prev = grid[i][j]



    print "Case #{}:".format(a+1)
    for el in grid:
        print "".join(el)
