import sys
from decimal import Decimal
def compute(C,F,X):
    t = 0.0
    r = 2.0
    #    print C
    #print F
    #print X
    while X/r >= (X/(r+F) + C/(r)):
        #        print X/r
        #print (X/(r+F) + C/(r))
        t += C/(r)
        r += F
    return "{0:.7f}".format(t + X/r)
                    
if __name__ == "__main__":
    f = sys.stdin
    if len(sys.argv) >= 2:
        fn = sys.argv[1]
        if fn != '-':
            f = open(fn)

    t = int(f.readline())
    for _t in xrange(t):
        l0=map(float,f.readline().split())
        C = l0[0]
        F = l0[1]
        X = l0[2]
        print "Case #" + str(_t+1) + ": " + str(compute(C,F,X))
