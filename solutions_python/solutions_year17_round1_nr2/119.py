import math

def solve(Q):
    try:
        while True:
            attempt = max(min(e[0] for e in q) for q in Q)
            releasable = sum(sum(1 for e in q if e[1]< attempt) for q in Q)
            if not releasable:
                break
            Q = [[e for e in q if e[1]>= attempt] for q in Q]
    except:
        return 0
    attempt = max(min(e[0] for e in q) for q in Q)
    Q2 = []
    for q in Q:
        l = min(e[1] for e in q)
        e = [i for i, e in enumerate(q) if e[1]==l and e[0]<=attempt][0]
        Q2+=[q[:e]+q[e+1:]]
    return 1+solve(Q2)

cnt = int(input())
for i in range(cnt):
    N, P = [int(s) for s in input().split(' ')]
    R = [int(s) for s in input().split(' ')]
    Q = [[int(s) for s in input().split(' ')] for j in range(N)]
    Q = [[(math.ceil((10*r[p])/(11*R[n])),math.floor((10*r[p])/(9*R[n]))) for p in range(P)] for n, r in enumerate(Q)]
    Q = [[qe for qe in q if qe[0]<=qe[1]] for q in Q]
    print('Case #' + str(i+1) +': '+str(solve(Q)))