for t in range(int(raw_input())):
    n = int(raw_input())
    a = []
    for i in xrange(n):
        a.append(raw_input())

    s = [0.]*n
    c = [0]*n
    for i in xrange(n):
        for j in xrange(n):
            b = a[i][j]
            if b != '.':
                s[i] += int(b)
                c[i] += 1

    wp = [s[i]/c[i] for i in xrange(n)]
    owp = [0.]*n

    for i in xrange(n):
        si = 0.
        ci = 0
        for j in xrange(n):
            b = a[i][j]
            if b != '.':
                ci += 1
                si += (s[j]-1+int(b))/(c[j]-1)
        owp[i] = si/ci

    oowp = [0.]*n
    for i in xrange(n):
        si = 0.
        ci = 0
        for j in xrange(n):
            b = a[i][j]
            if b != '.':
                ci += 1
                si += owp[j]
        oowp[i] = si/ci

    print 'Case #%d:' % (t+1)
    for i in xrange(n):
        print 0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i]
