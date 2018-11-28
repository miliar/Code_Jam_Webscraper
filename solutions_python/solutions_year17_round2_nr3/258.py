MAX_DIS = 21474836470000000
ShitTime = []

def ShitFunc(u, e, s, t):
    if e < 0: return
    ShitTime[u] = min(ShitTime[u], t)
    for v in range(N):
        if D[u][v] == -1: continue
        ShitFunc(v, e - D[u][v], s, t + float(D[u][v])/s)

def solve(N, Q, E, S, D, U, V):
    global ShitTime
    GraphNeedTime = []
    for u in range(N):
        ShitTime = [MAX_DIS for n in range(N)]
        ShitFunc(u, E[u], S[u], 0)
        ShitTime[u] = MAX_DIS
        GraphNeedTime.append(ShitTime)

    for k in range(N):
        for i in range(N):
            for j in range(N):
                GraphNeedTime[i][j] = min(GraphNeedTime[i][j], GraphNeedTime[i][k] + GraphNeedTime[k][j])

    res = []
    for q in range(Q):
        res.append(GraphNeedTime[U[q]][V[q]])
    return ' '.join(['%.6f'%x for x in res])


T = input()
for t in range(1, T + 1):
    N, Q = map(int, raw_input().split())
    E, S = [], []
    for n in range(N):
        e, s = map(int, raw_input().split())
        E.append(e)
        S.append(s)
    D = []
    for n in range(N):
        D.append(map(int, raw_input().split()))
    U, V = [], []
    for q in range(Q):
        u, v = map(int, raw_input().split())
        U.append(u - 1)
        V.append(v - 1)
    print 'Case #%d: %s'%(t, solve(N, Q, E, S, D, U, V))
