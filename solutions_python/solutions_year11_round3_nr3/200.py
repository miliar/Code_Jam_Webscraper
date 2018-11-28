#! /usr/bin/env python
# vim: set et ts=4 sw=4 ci cino=(0:
import sys
import os
import math
import binascii
                            
def main():
    f = open(sys.argv[1])
    ntest = int(f.readline().strip())

    for nt in xrange(ntest):
        l = f.readline().strip().split()  
        if len(l) !=  3:
            print "Error got 1", l
            sys.exit(1)

        n = int(l[0])
        lo = int(l[1])
        hi = int(l[2])
        
        if ( lo == 1 ):
            f.readline()
            print "Case #%d: %d" % (nt + 1, 1)
            continue

        
        nums = [ int(i) for i in f.readline().strip().split() ]
        if len(nums) !=  n:
            print "Error got 2", l
            sys.exit(1)

        lnums = [i for i in nums if i <= (lo * 2) ]
        hnums = [i for i in nums if i > (lo * 2) ]


        if ( len(lnums) == 0 ):
            nlcm = 1
        else:
            nlcm =  lcm( lnums )

        t = nlcm
        while( t < lo ):
            t += nlcm
        while (t <= hi) :
            res = True
            for i in hnums:
                if (t > i and (t % i) == 0) or ( t <= i and (i % t) == 0): 
                    pass
                else:
                    res = False
                    break

            if res == False:
                t += nlcm
            else:
                break

        if t <= hi:
            print "Case #%d: %d" % (nt + 1, t)
        else:
            print "Case #%d: NO" % (nt + 1)


def lcm(numbers):
    return reduce(__lcm, numbers)

def __lcm(a, b):
    return ( a * b ) / __gcd(a, b)

def __gcd(a, b):
    a = int(a)
    b = int(b)
    while b:
        a,b = b,a%b
    return a

if __name__ == "__main__":
    main()

