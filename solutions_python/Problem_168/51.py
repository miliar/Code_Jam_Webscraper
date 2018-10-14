way = {
    '^': (-1, 0),
    '>': (0, 1),
    'v': (1, 0),
    '<': (0, -1)
}
grid = []
R = 0
C = 0
r_mul = []
c_mul = []


def find_one(x, y, wayx, wayy):
    nowx = x
    nowy = y
    nowx += wayx
    nowy += wayy
    while nowx >= 0 and nowx < R and nowy >= 0 and nowy < C:
        if grid[nowx][nowy] == '.':
            nowx += wayx
            nowy += wayy
        else:
            return True
    return False

def solve(grid):
    global r_mul, c_mul
    ans = 0
    for r in xrange(R):
        grid_l = grid[r]
        for c in xrange(C):
            if grid_l[c] != '.':
                r_mul[r] += 1
                c_mul[c] += 1
    for r in xrange(R):
        grid_l = grid[r]
        for c in xrange(C):
            if grid_l[c] == '.':
                continue
            if find_one(r, c, way[grid_l[c]][0], way[grid_l[c]][1]):
                continue
            if r_mul[r] == 1 and c_mul[c] == 1:
                return 'IMPOSSIBLE'
            ans += 1
    return ans

def main():
    global grid
    global R, C
    global r_mul, c_mul
    T = input()
    for i in xrange(1, T + 1):
        grid = []
        R, C = map(int, raw_input().strip().split())
        for r in xrange(R):
            line = raw_input().strip()
            grid.append(line)
        r_mul = [0] * R
        c_mul = [0] * C
        print 'Case #{0}: {1}'.format(i, solve(grid))


if __name__ == '__main__':
    main()
