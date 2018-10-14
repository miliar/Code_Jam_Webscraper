import sys


fp = open(sys.argv[1])
T = int(fp.readline().strip())

def foo():
    [N, Q] = [int(x) for x in fp.readline().strip().split(" ")]
    E, S = [], []
    for i in range(N):
        [e, s] = [int(x) for x in fp.readline().strip().split(" ")]
        E.append(e)
        S.append(s)
    D = []
    for i in range(N):
        d = [int(x) for x in fp.readline().strip().split(" ")]
        D.append(d)
    U, V = [], []
    for i in range(Q):
        [u, v] = [int(x) for x in fp.readline().strip().split(" ")]
        U.append(u)
        V.append(v)
    mint = 1e13
    
    best = {}
    for city in range(N):
        best[city] = {}
    best[0][0] = 0.0
    for city in range(N):
        t = min(best[city].values())
        if city == N - 1:
            return t
        e, s = E[city], S[city]
        dist = 0
        for ncity in range(city + 1, N):
            dist += D[ncity - 1][ncity]
            if dist > e:
                break
            best[ncity][city] = t + float(dist) / float(s)




for case in range(T):
    print "Case #%d: %f" % (case + 1, foo())

fp.close()
