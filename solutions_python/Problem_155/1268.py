for t in xrange(1, input()+1):
    (m, s) = (lambda (x,y): (int(x), map(int, y)))(raw_input().split())
    a = reduce(lambda x,y: x+[x[-1]+y], s, [0])[:-1]
    print "Case #%d: %d"%(t, max(map(lambda (x,y): x-y, zip(range(m+1), a))))