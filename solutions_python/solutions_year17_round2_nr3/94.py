import sys
from collections import defaultdict
from heapq import heappush, heappop

# E is dict from node: (node, dist)


def runn(N, ES, D, U, V):
    queue = [(0, U, 0, .0000001, set())]
    ans = float('inf')
    while queue:
        d, u, e, s, visited = heappop(queue)
        if u == V:
            ans = min(d, ans)
            continue
        if d > ans:
            continue
        eu, su = ES[u]
        for v in range(u+1, u+2): # range(N)
            leg = D[u][v]
            if leg < 0 or v in visited:
                continue
            if e >= leg:
                heappush(queue, (d+1.*leg/s, v, e-leg, s, visited)) #  | set([v])
            if eu >= leg:
                heappush(queue, (d+1.*leg/su, v, eu-leg, su, visited)) #  | set([v])
    assert ans < float('inf')
    return ans

def run(N,Q,ES,D,UV):
    ans = [runn(N, ES, D, U, V) for U, V in UV]
    assert len(ans) == Q
    return ans

f = file(sys.argv[1],'r')
T = int(f.readline().strip())
for case in range(1,T+1):
    N,Q = [int(x) for x in f.readline().strip().split()]
    ES = [[int(x) for x in f.readline().strip().split()] for i in range(N)]
    D = [[int(x) for x in f.readline().strip().split()] for i in range(N)]
    UV = [[int(x)-1 for x in f.readline().strip().split()] for i in range(Q)]
    ans = run(N,Q,ES,D,UV)
    print 'Case #%d: %s' % (case, ' '.join(['%.7f' % x for x in ans]))
