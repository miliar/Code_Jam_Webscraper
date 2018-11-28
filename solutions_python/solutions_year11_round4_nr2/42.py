#!/usr/bin/env python

import sys

def debug(*args, **kwargs):
    ags = map(str, args)
    kags = map(lambda xs: "%s: %s" % xs, kwargs.iteritems())
    print >>sys.stderr, ", ".join(ags) + ", ".join(kags)

def line():
    return sys.stdin.readline().strip()

def intline():
    return map(int, line().split())

def comdiff(i,j,size,mass):
    half = float(size - 1)/2.0
    return [(float(i) - half)*mass, (float(j) - half)*mass]

def dosum(com, diff):
    com[0] += diff[0]
    com[1] += diff[1]

def dodiff(com, diff):
    com[0] -= diff[0]
    com[1] -= diff[1]

def total(rows,size,u,l):
    com = [0.0,0.0]
    for i in xrange(size):
        for j in xrange(size):
            y = u + i
            x = l + j
            z = rows[y][x]
            dosum(com, comdiff(i,j,size,z))
                
    for i in [0, size-1]:
        for j in [0, size-1]:
            y = u + i
            x = l + j
            z = rows[y][x]
            dodiff(com, comdiff(i,j,size,z))
    return com

def check(com):
    tol = 1e-4
    return abs(com[0]) < tol and abs(com[1]) < tol

def solve(r,c,rows):
    #return total(rows,5,1,1)
    for size in xrange(min(r,c), 2, -1):
        com = total(rows,size,0,0)
        if check(com):
            return size
        #print "Initial:", size,com

        for u in xrange(r - size + 1):
            #com = total(rows, size, u, 0)
            """
            print size
            print com
            """
            for l in xrange(0, c - size + 1):
                com = total(rows, size, u, l)
                if check(com):
                    return size
                continue
                
                for i in xrange(1, size - 1):
                    dodiff(com, comdiff(i, 0, size, rows[u + i][l]))
                    dosum(com, comdiff(i, size-1, size,
                                       rows[u + i][l + size]))
                dodiff(com, comdiff(0, 0, size, rows[u][l]))
                dodiff(com, comdiff(size - 1, 0, size,
                                    rows[u + size - 1][l]))

                dosum(com, comdiff(0, size-1, size, rows[u][l]))
                dosum(com, comdiff(size - 1, size-1, size,
                                    rows[u + size - 1][l]))

            if check(com):
                return size
    return "IMPOSSIBLE"

def main(argv):
    T = int(line())
    for caseno in xrange(T):
        r,c,d = intline()
        rows = []
        for _ in xrange(r):
            rows.append(map(lambda c: int(c) + d, line()))
        print "Case #%d: %s" % (caseno + 1, solve(r,c,rows)) 

if __name__ == "__main__":
    sys.exit(main(sys.argv))
