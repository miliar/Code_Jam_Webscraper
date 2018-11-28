import sys
import array

def prehl(b, c, x, y, num):
    c[x][y] = num
    for t in b[x][y]:
        prehl(b, c, t[0], t[1], num)

sx = [-1, 0, 0, 1]
sy = [0, -1, 1, 0]
for cas in range(int(sys.stdin.readline())):
    n, m = tuple([int(x) for x in sys.stdin.readline().split()])
    a = []
    for i in range(n):
        a.append([int(x) for x in sys.stdin.readline().split()])
    b = [[[] for x in range(m)] for y in range(n)]
    c = [[-1 for x in range(m)] for y in range(n)]

    for i in range(n):
        for j in range(m):
            al, x, y = a[i][j], -1, -1
            for k in range(4):
                s, t = sx[k] + i, sy[k] + j
                if s < 0 or s >= n or t < 0 or t >= m: continue
                if al > a[s][t]:
                    al, x, y = a[s][t], s, t
            if al < a[i][j]:
                b[x][y].append((i, j))
            else:
                c[i][j] = -2
    for i in range(n):
        for j in range(m):
            if c[i][j] == -2:
                prehl(b, c, i, j, i * m + j)
    r = 0
    w = {}
    for i in range(n):
        for j in range(m):
            if not c[i][j] in w:
                w[c[i][j]] = r
                r += 1

    print "Case #%d:" % (cas + 1)
    for i in range(n):
        for j in range(m):
            print ("%c" % chr(w[c[i][j]] + ord('a'))),
            if j == m - 1:
                print
