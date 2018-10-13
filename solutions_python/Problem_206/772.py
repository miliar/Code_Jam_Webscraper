def solve():
    T = int(input())

    for I in range(1, T + 1):
        d, n = map(int, input().split())
        m = 0.0001
        for i in range(n):
            k, s = map(int, input().split())
            r = (d - k) / s
            if r > m:
                m = r

        print('Case #%s: %s' % (I, d / m))


solve()
