RD = [1, -1, 0, 0]
CD = [0, 0, 1, -1]

T = int(raw_input())
for t in range(T):
    R, C = [int(x) for x in raw_input().strip().split()]
    grid = []
    for i in range(R):
        grid.append([int(x) for x in raw_input().strip().split()])

    def _find_path(r, c, rd, cd, min_h):
        if r < 0 or r >= R or c < 0 or c >= C:
            return True
        if grid[r][c] > min_h:
            return False
        return _find_path(r + rd, c + cd, rd, cd, min_h)

    def find_path(r, c):
        for rd, cd in zip(RD, CD):
            if _find_path(r, c, rd, cd, grid[r][c]) and _find_path(r, c, -rd, -cd, grid[r][c]):
                return True
        return False

    res = True
    for r in range(R):
        for c in range(C):
            # find a path out that doesn't go over something larger
            if not find_path(r, c):
                res = False
                break
        if not res:
            break

    print 'Case #%s: %s' % (t + 1, 'YES' if res else 'NO')
