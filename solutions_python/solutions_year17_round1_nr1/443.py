f = open('A-large.in')
fw = open('A-large.out', 'w')

T = int(f.readline())
for t in xrange(T):
    R, C = map(int, f.readline().split())
    grid = []
    for r in xrange(R):
        row = []
        row.extend(f.readline().strip())
        grid.append(row)
    first_row = None
    last_row = None
    for r in xrange(R):
        first_char = None
        last_char = None
        for c in xrange(C):
            if grid[r][c] == '?':
                if last_char is not None:
                    grid[r][c] = last_char
            else:
                if first_char is None:
                    first_char = grid[r][c]
                last_char = grid[r][c]
        if first_char is not None:
            for c in xrange(C):
                if grid[r][c] == '?':
                    grid[r][c] = first_char
                else:
                    break
            if first_row is None:
                first_row = grid[r]
            last_row = grid[r]
        elif last_row is not None:
            grid[r] = list(last_row)
    for r in xrange(R):
        if grid[r][0] == '?':
            grid[r] = list(first_row)
        else:
            break
    fw.write('Case #' + str(t + 1) + ':\n')
    for r in xrange(R):
        fw.write(''.join(grid[r]) + '\n')

fw.close()
f.close()
