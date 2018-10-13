import sys

in_file = sys.argv[1]

with open(in_file) as f:
    T = int(f.readline())
    for t in range(T):
        C, F, X = [float(n) for n in f.readline().strip().split()]
        v = 2.0
        if C >= X:
            res = X/v
        else:
            res = C/v
            c = C
            while c < X:
                if (X-c)/v > (X-c+C)/(v+F):
                    # buy farm
                    v += F
                    res += C/v
                else:
                    # no need to buy farm
                    res += (X-c)/v
                    c = X

        print 'Case #%s: %0.7f' % (t+1, res)



