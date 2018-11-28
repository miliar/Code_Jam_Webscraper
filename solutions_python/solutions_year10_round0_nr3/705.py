for case in xrange(1, int(raw_input()) + 1):
    print "Case #%d:" % case,

    r, k, n = map(int, raw_input().split())
    g = map(int, raw_input().split())
    g_count = len(g)

    #print r, k, n
    #print g

    euros = 0

    for i in xrange(r):
        used = g.pop(0)
        g.append(used)
        if used > k:
            break

        runs = 1
        while used <= k and runs < g_count:
            if g[0] + used > k:
                break
            x = g.pop(0)
            used += x
            g.append(x)
            runs += 1
        euros += used

    print euros
