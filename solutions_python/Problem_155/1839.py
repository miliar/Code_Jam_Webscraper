t = int(raw_input())

for x in xrange(t):
    s, line = raw_input().split()

    res = 0
    cur = 0

    for k, c in enumerate(line):
        if (cur < int(k)):
            diff = int(k) - cur
            cur += diff
            res += diff

        cur += int(c)

    print 'Case #%s:' % (x+1), res
