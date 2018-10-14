memoa = dict()
def a(m1, m2, n):
    if n <= m1 + m2 + 2:
        return 1
    if (m1, m2, n) in memoa:
        return memoa[(m1, m2, n)]
    if n % 2 == 0:
        memoa[(m1, m2, n)] = 2 * a(m1, m2, n//2)
    else:
        memoa[(m1, m2, n)] = a(m1, m2, n//2) + a(m1, m2, n//2+1)
    return memoa[(m1, m2, n)]


T = int(input())
for case in range(1, T+1):
    n, k = map(int, input().split())
    low, hi = 0, n
    for i in range(100):
        # print(low, hi)
        m = (low + hi) // 2
        if k >= a(m, m, n+1):
            hi = m
        else:
            low = m
    # print(low, hi)
    if k >= a(hi, hi-1, n+1):
        print(f"Case #{case}: {hi} {hi-1}")
    else:
        print(f"Case #{case}: {hi} {hi}")
