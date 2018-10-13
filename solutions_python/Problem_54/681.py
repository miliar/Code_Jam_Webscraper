#!/usr/bin/python

DEBUG = 0

def gcd(a, b):
    #print a, b
    if a < b: a, b = b, a
    if b == 1: return 1
    while 1:
        #print a, b
        a -= ((a / b) * b)
        if a == 0: return b
        #print "\t",a,b
        b -= ((b / a) * a)
        if b == 0: return a

C = int(raw_input().strip())
for c in range(C):
    values = [int(x) for x in raw_input().strip().split()]
    n_values = values.pop(0)
    assert n_values == len(values)
    if DEBUG: print values
    values = dict([(v, 1) for v in values]).keys()
    values.sort()
    if len(values) == 2:
        divisor = values[1] - values[0]
    else:
        diffs = []
        for n in range(len(values)-1):
            diffs.append(values[n+1] - values[n])
        #print diffs, values
        last_gcd = None
        for n in range(len(diffs)-1):
            if n == 0:
                last_gcd = gcd(diffs[0], diffs[1])
            else:
                last_gcd = gcd(last_gcd, diffs[n+1])
        divisor = last_gcd
    #print "d",divisor
    y = (values[-1] / divisor) * divisor - values[-1] + divisor
    if y == divisor: y = 0
    print "Case #%d: %d" % (c+1, y)
    if DEBUG:
        print "\t-> %s with divisor %d" % (`[x+y for x in values]`, divisor)
        for x in values:
            assert ((x+y) / divisor) * divisor == (x+y), "%d + %d is not divisible by %d" % (x, y, divisor)
    
#print gcd(900000000000000000001, 800000000000000000001)
