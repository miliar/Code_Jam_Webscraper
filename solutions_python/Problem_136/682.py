import sys

with open(sys.argv[1]) as f:
    T = int(f.readline())
    for i in range(T):
        vals = [float(x) for x in f.readline().split()]
        C = vals[0]
        F = vals[1]
        X = vals[2]
        offset = 0.0
        r = 2
        Tmin = X / r
        offset += C / r
        r += F
        t_Tmin = offset + X / r
        while t_Tmin < Tmin:
            Tmin = t_Tmin
            offset += C / r
            r += F
            t_Tmin = offset + X / r
        print "Case #%d: %f" % (i+1, Tmin)
