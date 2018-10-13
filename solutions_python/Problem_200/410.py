N = int(input())
for t in range(1, N + 1):
    n = int(input())
    m = 1
    while True:
        a = (n // m) % 10
        b = (n // (m * 10)) % 10
        if m >= n:
            break
        if b > a:
            n -= (a + 1) * m
            n = n // m + 1
            n = n * m - 1
        m *= 10
    print("Case #%d: %d" % (t, n))
