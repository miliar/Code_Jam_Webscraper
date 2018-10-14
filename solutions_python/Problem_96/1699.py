T = input()
for case in xrange(1,T+1):
    ins = raw_input().split()
    (N,S,p) = map(int,ins[:3])
    ts = map(int,ins[3:])

    t_normal = p+2*max(p-1,0)
    t_surprise = p+2*max(p-2,0)

    n = 0
    for t in ts:
        if t >= t_normal:
            n += 1
        elif t >= t_surprise and S > 0:
            S -= 1
            n += 1
    print "Case #%s: %s" % (case, n)
