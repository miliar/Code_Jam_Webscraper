import sys

PI = 3.141592653589793238462643383
N = int(sys.stdin.readline())
for num in range(N):
    N, K = map(int, sys.stdin.readline().split())
    rs = []
    hs = []
    rhs = []
    for i in range(N):
        r, h = map(int, sys.stdin.readline().split())
        rs.append(r)
        hs.append(h)
        rhs.append(r*h)
    rhs, rs, hs = zip(*reversed(sorted(zip(rhs, rs, hs))))
    best = 0
    s = sum(rhs[:K], 0)
    s2 = sum(rhs[:K-1], 0)
    mr = max(rs[:K])
    for i in range(N):
        r = rs[i]
        if i < K:
            val = PI * r * r + 2 * PI * s
            best = max(best, val)
        else:
            if r >= mr:
                val = PI * r * r + 2 * PI * (s2 + rhs[i])
                best = max(best, val)

    print('Case #{}: {}'.format(num+1, best))
        
