T = int(raw_input())
for t in range(T):
    C, F, X = raw_input().split()
    C = float(C)
    F = float(F)
    X = float(X)

    n = 0
    f = 2
    while True:
        A = X / (f + (n+1) * F)
        B = (X - C) / (f + n * F)
        if A > B:
            break
        n += 1

    ans = 0.0
    for i in range(n):
        ans += C / (f + i * F)

    ans += X / (f + n * F)
    print 'Case #%s: %s' % (t+1, ans)
