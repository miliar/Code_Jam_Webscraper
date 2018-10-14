import copy

for tc in range(1, int(raw_input())+1):
    n, m = map(int, raw_input().split())
    grid = [['.']*n for _ in range(n)]
    colmask = rowmask = d1mask = d2mask = 0
    for _ in range(m):
        c, x, y = raw_input().split()
        x, y = int(x)-1, int(y)-1
        grid[y][x] = c
        if c in 'xo':
            colmask |= 1 << x
            rowmask |= 1 << y
        if c in '+o':
            d1mask |= 1 << n-1+x-y
            d2mask |= 1 << x+y
    oldgrid = copy.deepcopy(grid)

    row = 0
    while row < n:
        if rowmask & (1<<row) == 0:
            col = 0
            while col < n and colmask & (1<<col):
                col += 1
            if grid[row][col] == '+':
                grid[row][col] = 'o'
            else:
                grid[row][col] = 'x'
            colmask |= 1<<col
        row += 1

    # bishop formations
    a = [(0, 0), (n-1, 0)]
    b = [(0, n-1), (n-1, n-1)]
    for x in range(1, n-1):
        a += [(x, 0), (x, n-1)]
        b += [(x, 0), (x, n-1)]
    c = [(0, 0), (0, n-1)]
    d = [(n-1, 0), (n-1, n-1)]
    for y in range(1, n-1):
        c += [(0, y), (n-1, y)]
        d += [(0, y), (n-1, y)]
    forms = [a, b, c, d]

    form = max(forms, key=lambda f: sum(grid[y][x] in '+o' for x, y in f))

    for x, y in form:
        if d1mask & (1 << n-1+x-y) or d2mask & (1 << x+y):
            continue
        if grid[y][x] == 'x':
            grid[y][x] = 'o'
        else:
            grid[y][x] = '+'
        d1mask |= 1 << n-1+x-y
        d2mask |= 1 << x+y

    changes = points = 0
    a = []
    for y in range(n):
        for x in range(n):
            if grid[y][x] in '+x':
                points += 1
            elif grid[y][x] == 'o':
                points += 2
            if grid[y][x] != oldgrid[y][x]:
                changes += 1
                a += [(grid[y][x], x+1, y+1)]
            
    print "Case #%d: %d %d" % (tc, points, changes)
    for i in a:
        print "%c %d %d" % i
