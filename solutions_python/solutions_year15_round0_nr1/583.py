for tc in xrange(int(raw_input())):
    n, l = tuple(raw_input().split())
    n, l = int(n), l
    c = r = 0
    for i in xrange(n + 1):
        if c < i:
            r += i - c
            c = i
        c += int(l[i])
    print "Case #%d: %d" % (tc + 1, r)
