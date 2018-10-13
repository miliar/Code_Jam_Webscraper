import math
for _ in xrange(input()):
    print  "Case #%d:" % (_+1),
    n, p = map(int, raw_input().split())
    R = map(int, raw_input().split())
    Q = [sorted(map(int, raw_input().split())) for i in xrange(n)]
    ids = [0]*n
    kmin = [None]*n
    kmax = [None]*n
    ans = 0
    def calc(i):
        j = ids[i]
        if j < p:
            kmin[i] = int(math.ceil(Q[i][j]/(1.1*R[i])))
            kmax[i] = int(math.floor(Q[i][j]/(0.9*R[i])))
            while Q[i][j] <= (kmin[i]-1)*1.1*R[i]:
                kmin[i] -= 1
            while (kmax[i]+1)*0.9*R[i] <= Q[i][j]:
                kmax[i] += 1
    for i in xrange(n):
        calc(i)
    while max(ids) < p:
        if max(kmin) <= min(kmax):
            ans += 1
            for i in xrange(n):
                ids[i] += 1
                calc(i)
        else:
            i = kmax.index(min(kmax))
            ids[i] += 1
            calc(i)
    print ans
