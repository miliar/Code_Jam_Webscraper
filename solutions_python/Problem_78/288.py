#! /usr/bin/env python
#coding=utf-8

import sys
import fractions

def main():
    if len(sys.argv) < 2:
        return
    f = open(sys.argv[1], "r").read().splitlines()
    t = int(f[0])
    for i in xrange(1, t + 1):
        z = f[i]
        s = z.split()
        n = int(s[0])
        pd = int(s[1])
        pg = int(s[2])
        
        if pg == 0:
            if pd != 0:
                print "Case #%d: Broken" % i
            if pd == 0:
                print "Case #%d: Possible" % i
            continue
        
        if pg == 100:
            if pd != 100:
                print "Case #%d: Broken" % i
            if pd == 100:
                print "Case #%d: Possible" % i
            continue

            
        #print n, pd, pg
        d = 100 / fractions.gcd(pd, 100)
        d = n / d * d
        dw = d * pd / 100
        
        g = 100 / fractions.gcd(pg, 100)
        gw = g * pg / 100
        k = max(d / g, dw / gw)
        g = g * (1 + k)
        gw = gw * (1 + k)
        
        #print d, dw, g, gw
        if d == 0 or g == 0 or gw - dw > g - d:
            print "Case #%d: Broken" % i
        else:
            print "Case #%d: Possible" % i

if __name__ == '__main__':
    main()
