for tc in xrange(1,1+input()):
    print 'Case #%d:'%tc,
    d,ho = map(int,raw_input().split())
    h = []
    for i in xrange(ho):
        a,b = map(int,raw_input().split())
        h.append(float(d-a)/b)
    x=max(h)
    print float(d)/x
