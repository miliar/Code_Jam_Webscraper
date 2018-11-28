import sys

with open(sys.argv[1]) as f:
    T = int(f.readline())

    for case in xrange(T):
        C, F, X = ( float(field) for field in f.readline().strip().split() )
        R = 2.0
        time = 0.0
        while True:
            if C/R + X/(R + F) < X/R:
                time += C/R
                R += F
            else:
                time += X/R
                break
        print "Case #%d:" % (case + 1), "%.7f" % time


        
