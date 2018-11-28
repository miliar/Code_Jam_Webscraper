
def solve_small(N, E, S, D):
    best = [None] * N
    best[0] = 0
    for i in xrange(N - 1):
        dist = 0
        for j in xrange(i + 1, N):
            road = D[j - 1]
            dist += road
            if dist > E[i]:
                break
            time = float(dist) / S[i] + best[i]
            if best[j] is None or time < best[j]:
                best[j] = time
    return best[-1]
    

T = int(raw_input())
for t in xrange(T):
    N, Q = map(int, raw_input().split(' '))
    ES = [map(int, raw_input().split(' ')) for _ in xrange(N)]
    D = [map(int, raw_input().split(' ')) for _ in xrange(N)]
    UV = [map(int, raw_input().split(' ')) for _ in xrange(Q)]
    D_small = [D[i][i + 1] for i in xrange(N - 1)]
    E, S = zip(*ES)
    res = solve_small(N, E, S, D_small)
    print 'Case #%d: %s' % (t + 1, res)
