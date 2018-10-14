MINE_INT = 9
MINE_STR = '*'

def calc_cell(grid, x, y):
    if grid[y][x] == MINE_STR:
        return MINE_INT

    cnt = 0
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if (dx or dy) and y + dy >= 0 and y + dy < Y and x + dx >= 0 and x + dx < X and grid[y + dy][x + dx] == MINE_STR:
                cnt += 1
    return cnt

def calc(grid):
    Y = len(grid)
    X = len(grid[0])
    cgrid = [[MINE_INT] * X for _ in xrange(0, Y)]
    for y in xrange(0, Y):
        for x in xrange(0, X):
            cgrid[y][x] = calc_cell(grid, x, y)

    return cgrid

def clear_neighbors(grid, x, y):
    Y = len(grid)
    X = len(grid[0])

    ngrid = [[grid[yi][xi] for xi in xrange(0, X)] for yi in xrange(0, Y)]

    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if (dx or dy) and y + dy >= 0 and y + dy < Y and x + dx >= 0 and x + dx < X and grid[y + dy][x + dx] == MINE_STR:
                ngrid[y + dy][x + dx] = '.'

    return ngrid

def solve(grid, M):
    Y = len(grid)
    X = len(grid[0])

    if M == 0:
        return grid
    if M < 0:
        return None

    cgrid = calc(grid)

    for y in xrange(0, Y):
        for x in xrange(0, X):
            if cgrid[y][x] != MINE_INT and cgrid[y][x] > 0:
                ngrid = clear_neighbors(grid, x, y)
                sol = solve(ngrid, M - cgrid[y][x])
                if sol:
                    return sol

    return None



if __name__ == '__main__':
    for caseno in xrange(int(raw_input())):
        Y, X, M = [int(s) for s in raw_input().split()]


        sol = None
        for y in xrange(0, Y):
            if sol:
                break
            for x in xrange(0, X):
                if sol:
                    break
                grid = [[MINE_STR] * X for _ in xrange(0, Y)]
                grid[y][x] = 'c'
                sol = solve(grid, X * Y - 1 - M)
                if sol:
                    break

        if sol:
            sol = '\n'.join([''.join(row) for row in sol])
        else:
            sol = 'Impossible'

        print 'Case #%d:\n%s' % (caseno + 1, sol)
