import fractions

c = input()
for i in xrange(c):
    y = map(int, raw_input().split())[1:]
    miny = min(y)
    y = map(lambda x: x - miny, y)
    gcd = y[0]
    for v in y[1:]:
        gcd = fractions.gcd(v, gcd)
    
    print "Case #%d: %s" % (i + 1, gcd - miny % gcd if miny % gcd else 0)

