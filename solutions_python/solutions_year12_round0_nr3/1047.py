#lol python
for k in xrange(input()):
    a, b = map(int, raw_input().split())
    ll = len(str(a))-1
    c = 0
    for i in xrange(a, b+1):
        q = i
        qqq = set()
        for j in xrange(ll):
            q = q/10+(q%10)*10**ll
            if q not in qqq and a<=q<=b and q>i:
                c += 1
            qqq.add(q)
    print "Case #%d: %d" % (k+1, c)