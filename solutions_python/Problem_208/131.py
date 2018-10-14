from heapq import *

def shortest(u):
    global n, horse, mat, dp, visited2
    dist = [(float('inf'), -1.0)] * n  # dist, traveled
    dist[u] = (0.0, 0.0)
    speed = float(horse[u][1])
    max_dist = horse[u][0]
    q = [(0.0, u)]
    visited = [False] * n
    while len(q) > 0:
        uu = q[0][1]
        heappop(q)
        if visited[uu]:
            continue
        visited[uu] = True
        cur, traveled = dist[uu]
        for vv in xrange(n):
            if dist[vv][0] > cur + mat[uu][vv] / speed and traveled + mat[uu][vv] <= max_dist:
                dist[vv] = (cur + mat[uu][vv] / speed, traveled + mat[uu][vv])
                heappush(q, (dist[vv], vv))
    for v in xrange(n):
        dp[u] = map(lambda x: x[0], dist)

T = int(raw_input())
for tt in xrange(T):
    n, q = map(int, raw_input().split())
    horse = [map(int, raw_input().split()) for _ in xrange(n)]
    mat = [map(lambda x: float('inf') if int(x) == -1 else float(x), raw_input().split()) for _ in xrange(n)]
    dp = [None] * n
    for u in xrange(n):
        shortest(u)
    for mid in xrange(n):
        for u in xrange(n):
            for v in xrange(n):
                if dp[u][v] > dp[u][mid] + dp[mid][v]:
                    dp[u][v] = dp[u][mid] + dp[mid][v]
    ans = []
    for _ in xrange(q):
        u, v = raw_input().split()
        u, v = int(u) - 1, int(v) - 1
        ans.append(dp[u][v])
    print 'Case #%s: %s' % (tt+1, ' '.join(map(str, ans)))
