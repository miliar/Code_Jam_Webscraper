for t in xrange(1, input() + 1):
    n = list(raw_input())
    for i in xrange(len(n) - 1, 0, -1):
        if n[i] < n[i-1] or n[i] == '0':
            n[i] = '9'
            n[i-1] = str(int(n[i-1]) - 1)
    for i in xrange(len(n) - 1, 0, -1):
        if n[i] < n[i-1]:
            n[i] = '9'
    print 'Case #%d: %d' % (t, int(''.join(n)))
