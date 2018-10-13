T = int(raw_input())
for t in xrange(1, T+1):
    s = set([str(i) for i in xrange(1, 17)])
    for board in xrange(2):
        r = int(raw_input())
        for i in xrange(1, 5):
            line = raw_input()
            if r == i:
                s &= set(line.split(' '))

    if len(s) == 1:
        print 'Case #%d: %s'% (t, list(s)[0])
    elif len(s) >= 2:
        print 'Case #%d: Bad magician!'% t
    else:
        print 'Case #%d: Volunteer Cheated!'% t

