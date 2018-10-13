def solve():
    r, c = map(int, raw_input().split())
    b = [raw_input().strip() for _ in xrange(r)]
    d = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
    ans = 0
    for i in xrange(r):
        for j in xrange(c):
            if b[i][j] != '.':
                dy, dx = d[b[i][j]]
                y, x = i + dy, j + dx
                while 0 <= y < r and 0 <= x < c:
                    if b[y][x] != '.':
                        break
                    y += dy
                    x += dx
                else:
                    ans += 1
                f = False
                for ni in xrange(r):
                    if i != ni and b[ni][j] != '.':
                        f = True
                for nj in xrange(c):
                    if j != nj and b[i][nj] != '.':
                        f = True
                if not f:
                    print "IMPOSSIBLE"
                    return
    print ans

T = int(raw_input())
for i in xrange(T):
    print "Case #%d:" % (i + 1),
    solve()
