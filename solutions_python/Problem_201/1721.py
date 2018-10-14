def sol(K, gaps):
    for i in xrange(K, 1, -1):
        M = max(gaps.keys(), key = int)
        L = (M - 1) / 2
        R = (M - 1) - L

        if gaps[M] == 1:
            del gaps[M]
        else:
            gaps[M] = gaps[M] - 1
        if L in gaps:
            gaps[L] = gaps[L] + 1
        else:
            gaps[L] = 1
        if R in gaps:
            gaps[R] = gaps[R] + 1
        else:
            gaps[R] = 1

    M = max(gaps.keys(), key = int)
    L = (M - 1) / 2
    R = (M - 1) - L
    return "%s %s" % (R, L)


t = long(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    line = raw_input()
    N, K = map(lambda x: int(x), line.split())
    print "Case #{}: {}".format(i, sol(K, {N: 1}))
