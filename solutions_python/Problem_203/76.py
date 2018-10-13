t = int(raw_input())

for case in xrange(1, t+1):
    rows, cols = map(int, raw_input().split())
    grid = []
    for _ in xrange(rows):
        grid.append(list(raw_input()))

    for r in xrange(rows):
        for c in xrange(cols):
            if grid[r][c].isupper():
                initial = grid[r][c]
                cl=c
                for cll in xrange(c-1, -1, -1):
                    # print 'cll', cll
                    if grid[r][cll] != '?':
                        break
                    cl = cll
                cr = c
                for crr in xrange(c+1, cols):
                    # print 'crr', crr
                    if grid[r][crr] != '?':
                        break
                    cr = crr

                # print 'range', cl, cr

                grid[r][cl:cr+1] = [initial.lower() for _ in xrange(cr+1-cl)]
                for ru in xrange(r-1, -1, -1):
                    if all(grid[ru][cc] == '?' for cc in xrange(cl, cr+1)):
                        grid[ru][cl:cr+1] = [initial.lower() for _ in xrange(cr+1-cl)]
                    else:
                        break
                for rb in xrange(r+1, rows):
                    if all(grid[rb][cc] == '?' for cc in xrange(cl, cr+1)):
                        grid[rb][cl:cr+1] = [initial.lower() for _ in xrange(cr+1-cl)]
                    else:
                        break

    result = '\n'.join(''.join(line) for line in grid)
    print("Case #{}:\n{}".format(case, result))