def gcd(a,b):
    if a < b: # need a >= b
        a,b = b,a
    while b != 0:
        a, b = b, (a-b*(a/b))
        if a < b:
            a,b = b,a
    return a

def debug(s, *args):
    if 0:
        print s % args

if __name__ == "__main__":
    import sys
    stream = open(sys.argv[1])

    testcases = int(stream.readline())
    for case in range(testcases):
        vals = [int(x) for x in stream.readline().split()]
        N = vals[0] # number of great events
        t = vals[1:] # time since each great event
        
        # T is the maximal common divisor possible from adding some y 
        # to each t[i].  It is thus also the greatest common divisor
        # of the differences between all t[i]
        # The y we add will be less than T.

        T = abs(t[0]-t[1])
        # Find gcd of all differences in values.
        for i in range(N-1):
            for j in range(i+1,N):
                T = gcd(T, abs(t[i]-t[j]))
        debug("T is %d", T)
        
        endval = list(t)
        diff = [0] * N
        for i in range(N):
            if t[i] % T != 0:
                endval[i] = T * ((t[i]/T)+1)
                diff[i] = endval[i] - t[i]
                
        debug("%s", t)
        debug("%s", endval)
        debug("%s", diff)

        print "Case #%d: %d" % (case+1, diff[0])
