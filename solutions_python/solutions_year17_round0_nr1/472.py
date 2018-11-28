import sys

import psyco; psyco.full()

def main():
    f = open(sys.argv[1], "rb")
    ncases = int(f.readline())
    for caseno in xrange(ncases):
        cakes, k = f.readline().strip().split()
        k = int(k)

        flipper = (1 << k) - 1
        row = 0
        for c in cakes:
            row *= 2
            if c == "-":
                row += 1
               
        nflips = 0
        for i in xrange(len(cakes)+1-k):
            if row & 1 == 1:
                nflips += 1
                row ^= flipper
                
            row >>= 1
            
        res = str(nflips)
        if row != 0:
            res = "IMPOSSIBLE"
            
        print "Case #%d: %s" % (caseno+1, res)
        
main()