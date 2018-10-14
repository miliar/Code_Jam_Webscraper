import sys
rl = lambda: sys.stdin.readline().strip()


T = int(rl())
for tcase in range(T):
    C, F, X = map(float, rl().split())
    farm = 0
    gain = 0.0
    elapsed = 0.0
    while gain < X:
        c1 = (X - gain) / (2 + farm * F)
        c2 = 0.0
        if gain >= C:
            c2 = (X - gain + C) / (2 + (farm + 1) * F)
            if c2 < c1:
                farm += 1
                gain -= C
            else:
                remain = X - gain
                income = (2.0 + farm * F)
                gain += min(income, remain)
                elapsed += min(1.0, remain / income)
        else:
            c2 = (C - gain) / (2 + farm * F)
            c2 += X / (2 + (farm + 1) * F)
            if c2 < c1:
                elapsed += ((C - gain) / (2 + farm * F))
                farm += 1
            else:
                remain = X - gain
                income = (2.0 + farm * F)
                gain += min(income, remain)
                elapsed += min(1.0, remain / income)
    print 'Case #%d: %.7lf' % (tcase + 1, elapsed)
