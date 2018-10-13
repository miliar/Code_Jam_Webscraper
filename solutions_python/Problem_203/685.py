import math


def solve():
    f = open("A-large.in", "r")
    T = int(f.readline())
    out = open("output.out", "w")

    for case in range(T):
        R, C = map(int, f.readline().split())
        grid = []
        for x in range(R):
            grid.append(' '.join(f.readline()).split())
        done = set()
        for y in range(R):
            for x in range(C):
                if grid[y][x] != '?' and grid[y][x] not in done:
                    l, r, u, d = 0, 0, 0, 0
                    while x - l - 1 >= 0 and grid[y][x - l - 1] == '?':
                        l = l + 1
                    while x + r + 1 < C and grid[y][x + r + 1] == '?':
                        r = r + 1
                    while y - u - 1 >= 0:
                        good = True
                        for j in range(x - l, x + r + 1, 1):
                            if grid[y - u - 1][j] != '?':
                                good = False
                                break
                        if good:
                            u = u + 1
                        else:
                            break
                    while y + d + 1 < R:
                        good = True
                        for j in range(x - l, x + r + 1, 1):
                            if grid[y + d + 1][j] != '?':
                                good = False
                                break
                        if good:
                            d = d + 1
                        else:
                            break
                    for j in range(y - u, y + d + 1):
                        for k in range(x - l, x + r + 1):
                            grid[j][k] = grid[y][x]
                    done.add(grid[y][x])

        print('Case #%d:' % (case + 1))
        out.write('Case #%d:\n' % (case + 1))
        for r in grid:
            print('%s' % (''.join(r)))
            out.write('%s\n' % (''.join(r)))


solve()
