
# 0:right 1:down 2:left 3:up
DIRECTION = {'>': 0, 'v': 1, '<': 2, '^': 3, }
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    T = int(raw_input())
    for t in xrange(1, T + 1):
        R, C = map(int, raw_input().split())
        grid = [raw_input() for _ in xrange(R)]
        count = 0
        for i in xrange(R):
            for j in xrange(C):
                if grid[i][j] == '.':
                    continue
                d = DIRECTION[grid[i][j]]
                y, x = i, j
                while True:
                    ny = y + dy[d]
                    nx = x + dx[d]
                    if nx < 0 or nx >= C or ny < 0 or ny >= R:
                        count += 1
                        break
                    if grid[ny][nx] != '.':
                        break
                    y, x = ny, nx

        raw_count = [0] * R
        column_count = [0] * C
        for i in xrange(R):
            for j in xrange(C):
                if grid[i][j] != '.':
                    raw_count[i] += 1
                    column_count[j] += 1
        f = False
        for i in xrange(R):
            for j in xrange(C):
                if grid[i][j] != '.' and raw_count[i] == 1 and column_count[j] == 1:
                    f = True
                    break
            if f:
                break
        if f:
            print "Case #%d: IMPOSSIBLE" % t
        else:
            print "Case #%d: %d" % (t, count)




