tt = int(raw_input())
for t in xrange(1, tt+1):
    s, kraw = raw_input().strip().split()
    k = int(kraw)
    x = [c for c in s]
    flips = 0
    fail = False
    for i in xrange(len(s)-k+1):
        if x[i] == '-':
            flips += 1
            for j in xrange(k):
                x[i+j] = '+' if x[i+j] == '-' else '-'
    for i in xrange(len(s)-k+1, len(s)):
        if x[i] == '-':
            fail = True
    ans = 'IMPOSSIBLE' if fail else str(flips)
    print 'Case #%d: %s' % (t, ans)
