cases = int(raw_input())

for i in xrange(cases):
    n, k = (int(x) for x in raw_input().split(" "))
    if k%(2**n) == 2**n-1:
        print "Case #%i: ON" % (i+1)
    else:
        print "Case #%i: OFF" % (i+1)
