lut = [1,4,9, 121, 484]
t = int(raw_input())
for i in xrange(t):
    a,b = map(int, raw_input().split())
    res = 0
    for n in lut:
        if n >= a and n <= b:
            res += 1
    print "Case #%s: %s" % (i+1, res)
