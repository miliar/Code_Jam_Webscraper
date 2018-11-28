import sys

fin = open(sys.argv[1])
fout = open(sys.argv[2], "w")

rl = lambda: fin.readline().strip()
ra = lambda type: map(type, rl().split())
ri = lambda: int(rl())

T = ri()
for ttt in xrange(T):
    X, S, R, t, N = ra(int)
    
    a = []
    rest = X
    for i in xrange(N):
        B, E, w = ra(int)
        a.append((w, E-B))
        rest -= E-B

    r = 0.0
    for w, L in sorted(a + [(0, rest)]):
        l = (R+w)*t
        if l > L:
            q = L/float(R+w)
            t -= q
            r += q
        else:
            q = (L-l)/float(S+w)
            r += t+q
            t = 0

    print >>fout, "Case #%d: %.6f" % (ttt+1, r)
