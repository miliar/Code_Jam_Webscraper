#!/usr/bin/python

import sys
import math
import itertools

pali_s = set([x for x in xrange(1, 10)])
lim = 10
for i in xrange(1, lim/2+1):
    for s in map("".join, itertools.product('0123456789', repeat=i)):
        if s[0] != '0':
            pali_s.add(int(s+s[::-1]))
            if i*2+1 < lim:
                for z in xrange(10):
                    pali_s.add(int(s+str(z)+s[::-1]))

def get_pali(a, b):
    sol = 0
    for i in xrange(a, b+1):
        if (i in pali_s) and (math.sqrt(i) in pali_s):
            sol = sol + 1
    return sol
        
def main(argv):
    if len(argv) != 2:
        print "Usage:", argv[0], "<input file>"
        return

    f = open(argv[1], "r")  
    o = open(argv[1]+".out", "w")  
    cc = int(f.readline())  
    print cc, "cases"  
    for c in xrange(cc):  
        s = f.readline()[:-1]
        a, b = map(int, s.split())
        ret = get_pali(a, b)
        o.write("Case #%d: %s\n" % (c+1, ret))  
    o.close()  
    f.close()

if __name__ == "__main__":
    main(sys.argv)
