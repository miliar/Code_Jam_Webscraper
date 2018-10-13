# Andy Rock
# April 14, 2017
# 
# Round 1A 2017: Problem B. 

for T in xrange(1, int(raw_input()) + 1):

    N, P = map(int, raw_input().split())
    R = map(int, raw_input().split())
    Q = [map(int, raw_input().split()) for _ in xrange(N)]

    poss = [[None for _ in xrange(P)] for __ in xrange(N)]
    for i in xrange(N):
        for j in xrange(P):
            # min lo st 500 * lo * 0.9 >= 900 
            # min lo st lo >= Q[i][j] * 10 / (R[i] * 9)
            lo = Q[i][j] * 10 / (R[i] * 11)
            if lo * R[i] * 10 < Q[i][j] * 9:
                lo += 1

            # max hi st 500 * hi * 1.1 <= 900
            hi = Q[i][j] * 10 / (R[i] * 9)
            if lo <= hi:
                poss[i][j] = (lo, hi)

        poss[i] = filter(lambda x : x, poss[i])
        poss[i].sort()

    idx = [0] * N

    ans = 0
    while True:
        good = True
        for i in xrange(N):
            good &= idx[i] < len(poss[i])
        if not good:
            break

        good = True
        lo, hi = poss[0][idx[0]]
        for i in xrange(1, N):
            while idx[i] < len(poss[i]) and poss[i][idx[i]][1] < lo:
                idx[i] += 1
            if idx[i] == len(poss[i]):
                good = False
                break

            if poss[i][idx[i]][0] > hi:
                for j in xrange(i):
                    while idx[j] < len(poss[j]) and poss[j][idx[j]][1] < poss[i][idx[i]][0]:
                        idx[j] += 1
                good = False
                break

            lo = max(lo, poss[i][idx[i]][0])
            hi = min(hi, poss[i][idx[i]][1])

        if good:
            ans += 1
            idx = [i + 1 for i in idx]

    print 'Case #%d: %s' % (T, ans)
