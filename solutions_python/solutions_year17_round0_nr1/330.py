T = int(raw_input())
for t in xrange(T):
    S, K = raw_input().split()
    s = len(S)
    k = int(K)
    c = map(lambda x: 1 if x == '-' else 0, S)
    a = []
    cur = 0
    count = 0
    for i in xrange(s-k+1):
        a.append(c[i] ^ cur)
        cur ^= a[i]
        count += a[i]
        if i >= k-1:
            cur ^= a[i-k+1]
    failed = False
    for i in xrange(s-k+1, s):
        if c[i] != cur:
            failed = True
            break
        if i >= k-1:
            cur ^= a[i-k+1]
    if failed:
        print 'Case #%d: IMPOSSIBLE' % (t+1)
    else:
        print 'Case #%d: %d' % (t+1, count)

