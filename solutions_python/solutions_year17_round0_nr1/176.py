def f():
    tc, = map(int, raw_input().split())
    for _tc in xrange(tc):
        s, k = raw_input().split()
        #print s, 
        s = [1 if c=='+' else 0 for c in s]
        k = int(k)
        n = len(s)
        res = 0
        for i in xrange(n-k+1): 
            if s[i] == 0: 
                res += 1
                s[i:i+k] = [1-s[j] for j in xrange(i, i+k)]
        if sum(s[n-k:n]) != k: res = None
        print 'Case #%d:' % (_tc+1,), res if res is not None else 'IMPOSSIBLE'
f()


