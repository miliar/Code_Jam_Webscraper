for tc in range(1, int(raw_input())+1):
    r, c = map(int, raw_input().split())
    grid = [list(raw_input()) for _ in range(r)]
    for y in range(r):
        for x in range(1, c):
            if grid[y][x] == '?':
                grid[y][x] = grid[y][x-1]
        for x in range(0, c-1)[::-1]:
            if grid[y][x] == '?':
                grid[y][x] = grid[y][x+1]
    for x in range(c):
        for y in range(1, r):
            if grid[y][x] == '?':
                grid[y][x] = grid[y-1][x]
        for y in range(0, r-1)[::-1]:
            if grid[y][x] == '?':
                grid[y][x] = grid[y+1][x]
    print "Case #%d:" % tc
    for row in grid:
        print ''.join(row)
