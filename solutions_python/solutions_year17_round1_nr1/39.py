t = int(raw_input())
for case in xrange(t):
    r, c = map(int, raw_input().split())
    grid = [list(raw_input()) for _ in xrange(r)]

    blank_rows = []
    for i in xrange(r):
        for c in grid[i]:
            if c != '?':
                current_c = c
                break
        else:
            blank_rows.append(i)
            continue
        for j in xrange(len(grid[i])):
            c = grid[i][j]
            if c != '?' and c != current_c:
                current_c = c
            else:
                grid[i][j] = current_c

    for i in blank_rows:
        if i == 0:
            for k in xrange(r):
                if k not in blank_rows:
                    for j in xrange(len(grid[k])):
                        grid[i][j] = grid[k][j]
                    break
        else:
            for j in xrange(len(grid[i])):
                grid[i][j] = grid[i - 1][j]

    print 'Case #{}:'.format(case + 1)
    for row in grid:
        print ''.join(row)
