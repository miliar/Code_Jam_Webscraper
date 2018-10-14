outp = "Case #{}: {:.6f}"

T = int(raw_input())

for _ in xrange(T):
    D, N = map(int, raw_input().split())
    m = 0
    for i in xrange(N):
        K, S = map(int, raw_input().split())
        m = max(float(D-K)/S, m)
    res = float(D)/m
    print outp.format(_ +1, res)