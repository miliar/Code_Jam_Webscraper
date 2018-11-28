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
        nrect = int(f.readline().strip())
        
        rects = []
        maxx = 0
        maxy = 0
        for r in xrange(nrect):
            l = [ int(x) for x in f.readline().strip().split() ]   
            if len(l) != 4:
                print "Error ", l
                sys.exit(1)
            xa = l[0]
            ya = l[1]
            xb = l[2]
            yb = l[3]
            if xa > xb:
                xa,xb = xb,xa
            if ya > yb:
                ya,yb = yb,ya

            if xb > maxx:
                maxx= xb
            if yb > maxy:
                maxy = yb

            rects.append( (xa, ya, xb, yb))
        
       
        grid = [[ 0 for x in xrange(maxx)] for y in xrange(maxy+2) ]

        for rec in rects:
            xa, ya, xb, yb = rec
            for x in xrange(xa-1, xb):
                for y in xrange(ya, yb+1):
                    grid[y][x] = 1

#        for xx in grid:
#            print xx

        found = True
        t = 0
        while found:
            found = False
            t += 1

            sy = maxy
            for sx in xrange(maxx-1, 0, -1):
                p = 0
                x = sx
                y = sy
                while True:
                    n = grid[y][x]
                    if p == 1 and n == 1:
                        grid[y+1][x] = 1
                    elif p == 0 and n == 0:
                        grid[y+1][x] = 0

                    if grid[y+1][x] == 1:
                        found = True
           
                    p = n
                    x += 1 
                    y -= 1
                    if x >= maxx or y < 0:
                        break

            sx = 0
            for sy in xrange(maxy, -1, -1):
                p = 0
                x = sx
                y = sy
                while True:
                    n = grid[y][x]
                    if p == 1 and n == 1:
                        grid[y+1][x] = 1
                    elif p == 0 and n == 0:
                        grid[y+1][x] = 0

                    if grid[y+1][x] == 1:
                        found = True
           
                    p = n
                    x += 1 
                    y -= 1
                    if x >= maxx or y < 0:
                        break

            #                found = doit( sx, sy, grid, grid, maxx )

#            print "New"
#            for xx in grid:
#               print xx

                    
               
        print "Case #%d: %d" % (nt + 1, t)


if __name__ == "__main__":
    main()

