with open('a.out', 'w') as f:
    t = int(input())
    for c in range(t):
        r, c_ = map(int, input().split())
        grid = [list(input()) for _ in range(r)]
        was = set()
        for y in range(r):
            for x in range(c_):
                if grid[y][x] != '?' and grid[y][x] not in was:
                    ch = grid[y][x]
                    was.add(ch)
                    x1 = x2 = x
                    y1 = y2 = y
                    while x1 > 0 and grid[y][x1-1] == '?':
                        x1 -= 1
                    while y1 > 0 and all(grid[y1-1][xx] == '?' for xx in range(x1, x2+1)):
                        y1 -= 1
                    while x2 < (c_ - 1) and all(grid[yy][x2+1] == '?' for yy in range(y1, y2+1)):
                        x2 += 1
                    while y2 < (r - 1) and all(grid[y2+1][xx] == '?' for xx in range(x1, x2+1)):
                        y2 += 1
                    for yy in range(y1, y2+1):
                        for xx in range(x1, x2 + 1):
                            grid[yy][xx] = ch
        print('Case #{0}:'.format(c + 1), file=f)
        for row in grid:
            print(''.join(row), file=f)
