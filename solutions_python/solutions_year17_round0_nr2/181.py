def f():
    tc, = map(int, raw_input().split())
    for _tc in xrange(tc):
        n = int(raw_input().strip())
        for i in xrange(1,20):
            div = 10**i
            h, t = divmod(n, div)
            if h == 0: break
            if h % 10 > t*10 // div:
                n = (h-1)*div + (div-1)

        print 'Case #%d: %d' % (_tc+1, n)
f()


