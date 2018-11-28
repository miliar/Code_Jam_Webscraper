nT = int(raw_input())

for t in range(1, nT + 1):
    s_max, s = raw_input().split()
    s_max = int(s_max)
    a = []
    for c in s:
        a.append(ord(c) - ord('0'))
    res = 0
    cur = 0
    for i, x in enumerate(a):
        while cur < i:
            cur += 1
            res += 1
        cur += x
    print 'Case #%d: %d' % (t, res)
