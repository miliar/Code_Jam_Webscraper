import sys

f = open(sys.argv[1])
fout = open(sys.argv[2], "w")

rl = lambda: f.readline().strip()
ra = lambda type: map(type, rl().split())
ri = lambda: int(rl())

count = lambda lam, x: float(len(filter(lam, x)))
avg = lambda x: sum(x) / float(len(x))

T = ri()
for t in xrange(T):
    N = ri()
    a = [rl() for i in xrange(N)]

    print >>fout, "Case #%d:" % (t+1)

    calc_wp = lambda games: count(lambda x: x=='1', games) / count(lambda x: x<>'.', games)

    wp = []
    for i in xrange(N):
        wp += [calc_wp(a[i])]

    wp1 = []
    for i in xrange(N):
        wp1 += [[calc_wp([a[i][k] for k in xrange(N) if k != j]) for j in xrange(N)]]

    owp = []
    for i in xrange(N):
        owp += [avg([wp1[j][i] for j in xrange(N) if i != j and a[i][j] != '.'])]

    oowp = []
    for i in xrange(N):
        oowp += [avg([owp[j] for j in xrange(N) if i != j and a[i][j] != '.'])]

    for i in xrange(N):
        rpi = 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i]
        print >>fout, rpi
