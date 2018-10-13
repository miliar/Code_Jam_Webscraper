t = int(raw_input())
for i in xrange(1,t + 1):
    l1 = raw_input().split(' ')
    c = float(l1[0])
    f = float(l1[1])
    x = float(l1[2])
    nc = 0
    segs = 0.0
    a = x / 2
    b = 0
    if x <= c:
        segs = x / 2
    else:
        count = 0
        while a > b:
            b = 0
            count += 1
            for r in xrange(0,count):
                b = b + (c / (2 + (r * f)))
            b = b + x / (2 + (count * f))
            if a < b:
                break
            else:
                a = b
                b = 0
        segs = a
    print 'Case #%d: %.7f' % (i, segs)