for t in range(int(raw_input())):
    n, d = map(int, raw_input().split())

    a = [None]*n

    for i in xrange(n):
        p, v = map(int, raw_input().split())
        a[i] = (p, v)

    a = sorted(a, key=lambda b: b[0])
    for i in xrange(n):
        s = (a[i][1]-1)*d/2.
        a[i] = (a[i][0]-s, a[i][0]+s, s)

    while True:
        l = len(a)
        for i in xrange(l-1):
            r = a[i+1][0] - a[i][1] - d
            if r < 0:
                r = -r
                if a[i][2] > a[i+1][2]:
                    if a[i][2] - a[i+1][2] >= r:
                        a[i+1] = (a[i][0], a[i+1][1]+r, a[i][2])
                    else:
                        o = (r - (a[i][2] - a[i+1][2]))/2.
                        a[i+1] = (a[i][0]-o, a[i+1][1]+o+(a[i][2] - a[i+1][2]), a[i][2]+o)
                else:
                    if a[i+1][2] - a[i][2] >= r:
                        a[i+1] = (a[i][0]-r, a[i+1][1], a[i+1][2])
                    else:
                        o = (r - (a[i+1][2] - a[i][2]))/2.
                        a[i+1] = (a[i][0]-o-(a[i+1][2] - a[i][2]), a[i+1][1]+o, a[i+1][2]+o)

                a[i] = None

        a = [b for b in a if b != None]
        if len(a) == l:
            break

    res = max([b[2] for b in a])


    print 'Case #%d: %f' % (t+1, res)
