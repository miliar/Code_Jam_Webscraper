T = int(raw_input())

for c in xrange(T):
    C, F, X = [float(x) for x in raw_input().split()]

    total = 0.0
    cur = 2

    while (C/cur + X / (F + cur)) < (X/cur):
        total += C/cur
        cur += F
    
    total += X/cur
    print "Case #%d: %0.7f" % (c+1, total)
