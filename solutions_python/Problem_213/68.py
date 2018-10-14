import collections
def solve(N, C, G):
    if N == 1:
        return len(G)
    B = collections.Counter([g[0] for g in G])
    A = collections.Counter([g[1] for g in G])
    cum = 0
    mc = A.most_common(1)[0][1]
    for i in range(1, N+1):
        cum+=B[i]
        mc=max(mc, (cum+i-1)//i)
    prom = 0
    for i in range(1, N+1):
        prom+=max(0, B[i]-mc)
    return str(mc) + ' ' + str(prom)

cnt = int(input())
for i in range(cnt):
    N, C, M = [int(j) for j in input().split(' ')]
    G=[[int(j) for j in input().split(' ')] for m in range(M)]
    print('Case #' + str(i+1) +': '+str(solve(N, C, G)))