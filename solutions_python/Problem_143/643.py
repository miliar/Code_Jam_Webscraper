t = int(raw_input()) + 1
for kase in xrange(1, t):
    ans = 0
    a, b, k = map(int ,raw_input().split())
    for i in xrange(0, a):
        for j in xrange(0, b):
            if i & j < k:
                #print a, b
                ans +=1
    print 'Case #%s: %s' % (kase, ans)
