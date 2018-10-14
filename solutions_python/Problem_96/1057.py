for k in xrange(input()):
    vals = map(int, raw_input().split())
    n, s, p = vals.pop(0), vals.pop(0), vals.pop(0)
    c = 0
    for v in vals:
        oc = c
        if v%3 == 0:
            if p-v/3 == 1 and s>0 and v/3>0:
                c += 1
                s -= 1
            elif v/3 >= p:
                c += 1
        elif v%3 == 1:
            if v/3+1 >= p:
                c += 1
        elif v%3 == 2:
            if p-(v/3+1) == 1 and s>0:
                c += 1
                s -= 1
            elif v/3+1 >= p:
                c += 1
    print "Case #%d: %d" % (k+1, c)