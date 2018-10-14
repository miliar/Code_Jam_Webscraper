import sys
sin = sys.stdin
T = int(sin.readline().strip())
for i in xrange(1, T+1):
    N, Q = map(int, sin.readline().strip().split())
    E, S = [], []
    for j in xrange(N):
        Ei, Si = map(long, sin.readline().strip().split())
        E.append(Ei)
        S.append(Si)
    D = []
    for j in xrange(N):
        Dij = map(long, sin.readline().strip().split())
        D.append(Dij)
    #print 'E:{0}, S:{1}, D:{2}'.format(E, S, D)
    ts = []
    for k in xrange(Q):
        Uk, Vk = map(int, sin.readline().strip().split())
        combs = []
        for j in xrange(N-1):
            d = D[j][j+1]
            Si = S[j]
            Ei = E[j]
            t = d*1.0/Si
            dleft = Ei - d
            new_combs = []
            if j == 0:
                new_combs.append((t, Si, dleft))
            else:
                for comb in combs:
                    new_combs.append((t+comb[0], Si, dleft))
                    if comb[2] >= d:
                        new_combs.append((comb[0] + d*1.0/comb[1], comb[1], comb[2]-d))
            #print 'New combs: {0}, d:{1}, t:{2}, Ei:{3}, Si:{4}'.format(new_combs, d, t, Ei, Si)
            combs = new_combs
        #print combs
        mint = sorted(combs, key=lambda x: x[0])[0][0]
        ts.append('{0:.6f}'.format(round(mint*10**6)/10**6))
    print 'Case #{0}: {1}'.format(i, ' '.join(ts))

    """
    for j in xrange(Q):
        Uk, Vk = map(int, sin.readline().strip().split())
        t = 0
        d = 0
        for k in reversed(xrange(Uk, Vk)):
            if k == Vk - 1:
                continue
            dk = Dij[k][Vk]
            tk = dk*1.0/Ei[k] if Si[k] >= tk
            for p in xrange(k+1, Vk):
                dk = Dij[k][p]
                if dk > Si[k]:
                    break
    """
