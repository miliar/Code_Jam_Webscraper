

T = int(raw_input())

for i in xrange(T):
    [R, C] = map(int, raw_input().split())
    grid = []
    unknown_count = 0
    for j in xrange(R):
        this_row = list(raw_input())
        unknown_count += this_row.count("?")
        grid.append(this_row)

    # pass 1 -- expand horizontally
    for x in xrange(R):
        for y in xrange(C):
            if grid[x][y] != "?":
                sym = grid[x][y]
                xit = x-1
                while xit >= 0 and grid[xit][y] == "?":
                    grid[xit][y] = sym
                    xit-=1
                xit = x+1
                while xit < R and grid[xit][y] == "?":
                    grid[xit][y] = sym
                    xit+=1

    # pass 2 -- expand downwards
    for x in xrange(R):
        for y in xrange(1, C):
            if grid[x][y] == "?":
                if (grid[x][y-1] != "?"):
                    grid[x][y] = grid[x][y-1]

    # pass 3 -- more strays, expand upwards
    for x in xrange(R):
        for y in xrange(C - 1, -1, -1):
            if grid[x][y] == "?":
                if (grid[x][y+1] != "?"):
                    grid[x][y] = grid[x][y+1]

    print "Case #%d:" % (i + 1)
    for row in grid:
        print "".join(row)
