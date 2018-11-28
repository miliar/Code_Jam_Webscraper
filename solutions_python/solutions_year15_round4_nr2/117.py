from sys import stdin

T = int(stdin.readline())
for no in range(T):
    N, V, X = stdin.readline().split()
    N = int(N)
    V = float(V)
    X = float(X)

    tmp = [
        map(float, stdin.readline().split())
        for i in range(N)
    ]
    R, C = zip(*sorted(tmp, key=lambda x: x[1]))

    l = 0
    r = 2e8
    while r - l > 1e-9:
        m = (l + r) / 2

        p = [m * R[i] / V for i in range(N)]

        if sum(p) < 1:
            l = m
            continue

        minx = 0
        maxx = 0

        s = 0
        for i in range(N):
            if s + p[i] <= 1:
                s += p[i]
                minx += p[i] * C[i]
            else:
                minx += (1 - s) * C[i]
                break

        s = 0
        for i in range(N-1, -1, -1):
            if s + p[i] <= 1:
                s += p[i]
                maxx += p[i] * C[i]
            else:
                maxx += (1 - s) * C[i]
                break

        if minx <= X and maxx >= X:
            r = m
        else:
            l = m

    print 'Case #{}:'.format(no + 1),
    if l > 1.5e8:
        print 'IMPOSSIBLE'
    else:
        print '{:.9f}'.format((l+r) / 2)
