import sys

T = int(sys.stdin.readline().strip())


for i in xrange(T):
    C, F, X = [float(x) for x in sys.stdin.readline().strip().split(" ")]
    
    t = 0.0
    r = 2.0

    while True:
        t_f = C/r + X/(r+F)
        t_n = X/r

        if t_f < t_n:
            t += C/r
            r += F
        else:
            t += X/r
            break

    print "Case #%d: %.7f" % (i+1,  t)



    
