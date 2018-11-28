t = int(raw_input())
for case in xrange(1, t+1):
    r, c = map(int, raw_input().split())
    grid = [list(raw_input()) for _ in xrange(r)]
    found = False
    for row in xrange(r):
        last_val = None
        for col in xrange(c):
            val = grid[row][col]
            if last_val is None:
                if val != "?":
                    last_val = val
                    for col2 in xrange(col):
                        grid[row][col2] = val
            else:
                if val == "?":
                    grid[row][col] = last_val
                else:
                    last_val = val
        if not found:
            if last_val is not None:
                found = True
                for col in xrange(c):
                    val  = grid[row][col]
                    for row2 in xrange(row):
                        grid[row2][col] = val
        else:
            if last_val is None:
                for col in xrange(c):
                    grid[row][col] = grid[row-1][col]
    print "Case #"+str(case)+":"
    for row in xrange(r):
        print "".join(grid[row])


