T = int(raw_input().strip())

for t in xrange(1, T + 1):
    (N, K) = map(int, raw_input().strip().split(' '))
    Q = [N]
    T = {}
    D = {N: 1}
    i = 0
    while Q:
        n = Q.pop()
        if n == 0:
            continue
        i += 1
        a = n / 2
        if n & 1 or not n:
            b = a
        else:
            b = a - 1
        if not a in D:
            Q = [a] + Q
            D[a] = 0
        if not b in D:
            Q = [b] + Q
            D[b] = 0
        T[n] = (a, b)
        D[a] += D[n]
        D[b] += D[n]
    keys = T.keys()
    keys.sort()
    keys.reverse()
    c = 0
    for i in range(len(keys)):
        k = keys[i]
        c += D[k]
        if c >= K:
            (a, b) = T[k]
            break
    print 'Case #%d: %d %d' % (t, a, b)
