for cs in xrange(int(raw_input())):
    s_max, levels = raw_input().split()
    s_max = int(s_max)
    levels = map(int, list(levels))

    now = 0
    res = 0
    for i in xrange(len(levels)):
        if now < i:
            res += i-now
            now = i + levels[i]
        else:
            now += levels[i]

    print 'Case #%d: %d' % (cs+1, res)
            

