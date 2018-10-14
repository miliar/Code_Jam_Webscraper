DELTA_X = [-1,  0, 0, 1]
DELTA_Y = [ 0, -1, 1, 0]

def main():
    n, m = map(int, raw_input().split())
    grid = [raw_input() for i in xrange(n)]
    row_count, column_count = [0] * n, [0] * m
    for i in xrange(n):
        for j in xrange(m):
            if grid[i][j] != '.':
                row_count[i]    += 1
                column_count[j] += 1
    result = 0
    for i in xrange(n):
        for j in xrange(m):
            if grid[i][j] != '.':
                d = "^<>v".index(grid[i][j])
                x, y = i + DELTA_X[d], j + DELTA_Y[d]
                while 0 <= x < n and 0 <= y < m and grid[x][y] == '.':
                    x += DELTA_X[d]
                    y += DELTA_Y[d]
                if not (0 <= x < n and 0 <= y < m):
                    if row_count[i] == 1 and column_count[j] == 1:
                        return 'IMPOSSIBLE'
                    result += 1
    return result

for t in xrange(input()):
    print "Case #%d: " %(t + 1), main()
