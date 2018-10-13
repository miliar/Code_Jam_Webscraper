tests = int(raw_input())

for test in xrange(tests):
    n, q = map(int, raw_input().split())
    horses = []
    for i in xrange(n):
        horses.append(map(int, raw_input().split()))
    c = []
    for i in xrange(n):
        c.append(map(int, raw_input().split()))
    for k in xrange(n):
        for i in xrange(n):
            for j in xrange(n):
                if c[i][k] != -1 and c[k][j] != -1:
                    d = c[i][k] + c[k][j]
                    c[i][j] = d if d < c[i][j] or c[i][j] == -1 else c[i][j]
    h = [[-1]*n for _ in xrange(n)]
    for i in xrange(n):
        for j in xrange(n):
            if c[i][j] == -1 or horses[i][0] < c[i][j]:
                h[i][j] = -1
                continue
            h[i][j] = float(c[i][j])/float(horses[i][1])
    for k in xrange(n):
        for i in xrange(n):
            for j in xrange(n):
                if h[i][k] != -1 and h[k][j] != -1:
                    d = h[i][k] + h[k][j]
                    h[i][j] = d if d < h[i][j] or h[i][j] == -1 else h[i][j]
    print "Case #{}:".format(test+1),
    for i in xrange(q):
        u, v = map(int, raw_input().split())
        print h[u-1][v-1],
    print ""
