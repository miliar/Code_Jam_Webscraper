nT = int(raw_input())

for t in range(1, nT + 1):
    d = int(raw_input())
    a = map(int, raw_input().split())

    res = 10 ** 18
    for v in range(1, 1001):
        cur = v
        for x in a:
            cur += (x + v - 1) / v - 1
        if cur < res:
            res = cur
    print 'Case #%d: %d' % (t, res)
