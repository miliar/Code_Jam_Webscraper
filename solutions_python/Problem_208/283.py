T = int(raw_input())

for case in range(T):
    N, Q = map(int, raw_input().split())
    E = []
    S = []
    for n in range(N):
        e, s = map(int, raw_input().split())
        E.append(e)
        S.append(s)
    graph = dict()
    for n in range(N):
        dists = map(int, raw_input().split())
        for m in range(N):
            if dists[m] != -1:
                graph[(n+1)] = dict()
                graph[(n+1)][m+1] = dists[m]
    for q in range(Q):
        U, V = map(int, raw_input().split())
    D = [0]
    for n in range(N-1):
        E[n] += D[n]
        D.append(D[-1] + graph[n+1][n+2])

    time = [{0:D[1]/float(S[0])}]
    for n in range(N-2):
        horse = n+1
        src = D[n+1]
        dst = D[n+2]
        res = {}
        for t in time[-1].keys():
            if E[t] >= dst:
                res[t] =(dst-src)/float(S[t]) + time[-1][t]
        if E[horse] >= dst:
            res[horse] = (dst-src)/float(S[horse]) + min(time[-1].values())
        time.append(res)
    ret = min(time[-1].values())



    print "Case #{0}: {1}".format(case+1, ret)

