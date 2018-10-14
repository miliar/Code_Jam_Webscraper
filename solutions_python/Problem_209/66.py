import numpy as np

def solve():
    N,K = [int(v) for v in input().split()]
    P = []
    for i in range(N):
        ri,hi = [int(v) for v in input().split()]
        P.append([ri,hi])
    P = sorted(P,key=lambda p: p[0])
    m = 0
    o = [p[0]*p[1] for p in P[:K-1]]
    for i in range(K-1,N):
        o = sorted(o,reverse=True)
        m = max(m, 2*np.pi*(sum(o[:K-1])+P[i][0]*P[i][1])+np.pi*P[i][0]*P[i][0])
        o.append(P[i][0]*P[i][1])
    return m

        

T = int(input())
for t in range(1, T + 1):
    print('Case #%d: %.9f' % (t,solve()))


