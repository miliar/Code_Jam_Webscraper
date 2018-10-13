prefix = "Case #%d:"

def devide(n):
    if n % 2 == 0:
        return (n/2, n/2-1)
    else:
        return (n/2, n/2)

def solve(t):
    N, K = map(int, raw_input().split())
    q1 = {N: 1}
    while K > 0:
        q2 = {k:v for k, v in q1.items()}
        q1 = {}
        for k in sorted(q2.keys())[::-1]:
            v = q2[k]
            a, b = devide(k)
            q1[a] = q1.get(a, 0) + v
            q1[b] = q1.get(b, 0) + v
            K -= v
            if (K <= 0):
                print prefix%t, max(a, b), min(a, b)
                return

T = int(raw_input())
for t in xrange(1, T+1):
    solve(t)
