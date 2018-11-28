T = int(raw_input())
for t in xrange(1, T+1):
    segs = raw_input().split()
    s_max = int(segs[0])
    a = [int(x) for x in segs[1]]
    f = 0
    p = 0

    s = 0
    while s != len(a):
        if p < s:
            f += s-p
            p += s-p

        else:
            p += a[s]
            s += 1
    print 'Case #{0}: {1}'.format(t, f)
