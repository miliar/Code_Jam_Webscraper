import sys

f = open(sys.argv[1])
fout = open(sys.argv[2], "w")

rl = lambda: f.readline().strip()
ra = lambda type: map(type, rl().split())
ri = lambda: int(rl())

T = ri()
for t in xrange(T):
    N, L, H = ra(int)
    freq = ra(int)

    r = "NO"
    for i in xrange(L, H+1):
        if all([max(i, fr) % min(i, fr) == 0 for fr in freq]):
            r = str(i)
            break

    print >>fout, "Case #%d: %s" % (t+1, r)
