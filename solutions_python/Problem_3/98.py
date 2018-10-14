import sys
from math import pi, acos, asin, sin, sqrt
import psyco
psyco.full()

FILE = 'C-small-attempt1(2).in'
fp = open(FILE, 'r')
sys.stdout = open(FILE + '.out', 'w')

def rs():
    return fp.readline()[:-1]

def ri():
    return int(fp.readline())

def raf():
    return [float(s) for s in rs().split()]

def ins(lst, (x, y)):
    if not any(abs(xx - x) < 1e-6 and abs(yy-y) < 1e-6 for xx, yy in lst):
        lst.append((x, y))
        
    

ncases = int(fp.readline())

for ncase in xrange(1, ncases+1):
    f, R, t, r, g = raf()
    RI = R - t
    
    emptyarea = 0
    
    complete = 0
    partial = 0
    ix = 0
    x = float(r)
    while x < RI:
        iy = 0
        y = float(r)
        while True:
            xx = x + g
            yy = y + g
            RIF = RI-f
            RI2 = (RIF)**2
            nx = x + f
            ny = y + f
            nxx = xx - f
            nyy = yy - f
            if nx ** 2 + ny ** 2 > RI2:
                break
            if nxx**2 + nyy**2 > RI2:
                cy2 = RI2 - nx**2
                cyy2 = RI2 - nxx**2
                cx2 = RI2 - ny**2
                cxx2 = RI2 - nyy**2
                points = []
                if cy2 > 0:
                    cy = sqrt(cy2)
                    if ny <= cy <= nyy: ins(points, (nx, cy))
                if cyy2 > 0:
                    cyy = sqrt(cyy2)
                    if ny <= cyy <= nyy: ins(points, (nxx, cyy))
                if cx2 > 0:
                    cx = sqrt(cx2)
                    if nx <= cx <= nxx: ins(points, (cx, ny))
                if cxx2 > 0:
                    cxx = sqrt(cxx2)
                    if nx <= cxx <= nxx: ins(points, (cxx, nyy))
                points.sort()
                if len(points) != 2:
                    #sys.stderr.write('NPoints: %d' % len(points))
                    continue
                cx1, cy1 = points[0]
                cx2, cy2 = points[1]
                ang1 = asin(cy1 / float(RIF))
                ang2 = asin(cy2 / float(RIF))
                ang = abs(ang1 - ang2)
                segarea = ((RI2 * ang) - (RI2 * sin(ang))) / 2.0
                emptyarea += segarea
                if cx1 == nx:
                    temp1 = ((cy1-ny) + (cy2-ny))
                    temp2 = (cx2-nx)
                    if temp1 > 0 and temp2 > 0:
                        area = (temp1 * temp2) / 2.0
                        emptyarea += area
                        partial += 1
                        #sys.stderr.write('Partial at: %d, %d: %f\n' % (ix, iy, area))
                else:
                    temp1 = ((nxx-cx1) + (nxx-cx2))
                    temp2 = (nyy-cy2)
                    if temp1 > 0 and temp2 > 0:
                        area = (temp1 * temp2) / 2.0
                        area = (g - 2*f) ** 2 - area
                        emptyarea += area
                        partial += 1
                        #sys.stderr.write('Partial at: %d, %d: %f\n' % (ix, iy, area))
            else:
                temp = g - 2*f
                if temp > 0:
                    complete += 1
                    emptyarea += temp ** 2
            iy += 1    
            y += g + 2*r
        ix += 1
        x += g + 2*r
        
    totalarea = pi * R**2
    prob = (totalarea - emptyarea * 4.0) / float(totalarea)
    print 'Case #%d: %1.6f' % (ncase, prob)
    #sys.stderr.write('Complete: %d, Partial: %d\n' % (complete, partial))
    