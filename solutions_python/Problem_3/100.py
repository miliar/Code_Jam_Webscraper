#import psyco; psyco.full()

from math import sqrt, atan2, pi
def process(f, rr, t, r, g):
    # we can calculate the probability as (area of f-expanded shape) / (area of outer circle)

    rri = rr - t - f           # inner radius
    if rri**2 <= 2 * r**2: return 1.0    # gap is beyond inner radius
    if g - 2*f <= 0: return 1.0          # gap is too small so fly cannot escape

    def areaf(i): # calculate area of slice of quarter of circle between x=0 and x=i
        # INT 0..i {sqrt(r^2 - x^2) dx}
        # = 0..i (x^2 sqrt(r^2 - x^2) + r^2 atan(x / sqrt(r^2 - x^2))) / 2
        if i < 0: return 0
        if i > rri: return pi / 4
        ri = sqrt(rri**2 - i**2)
        return (i * ri + rri**2 * atan2(i, ri)) / 2

    def area(x1, y1, x2, y2): # calculate circle area of rectangle (x1,y1)-(x2,y2)
        #  (1)       (2)       (3)       (4)       (5)
        #  @@@@@@@@  @@@@|...  ........  .....|..  ........
        #  @@@@@@@@  @@@@|@@.  @@@@....  @@...|..  ........
        #  @@@@@@@@  @@@@|@@@  @@@@@@@.  @@@@.|..  ........
        #  @@@@@@@@  @@@@|@@@  @@@@@@@@  @@@@@|..  ........
        #  --------  ----+---  --------  -----+--  -------- lower bound
        #  @@@@@@@@  @@@@|@@@  @@@@@@@@  @@@@@|..  @@@.....
        #               x1 adjust           x2 adjust
        if x1 > x2: x1, x2 = x2, x1
        if y1 > y2: y1, y2 = y2, y1
        #print '\tx1=%f x2=%f y1=%f y2=%f rri=%f' % (x1, x2, y1, y2, rri)

        maxy1 = sqrt(rri**2 - min(rri, x2)**2)
        maxy2 = sqrt(rri**2 - min(rri, x1)**2)
        #print '\tmaxy1=%f maxy2=%f' % (maxy1, maxy2)
        rectarea = 0.0
        if maxy2 >= y2:
            if maxy1 >= y2: # optimization!
                return (y2 - y1) * (x2 - x1)
            prevx1 = x1
            x1 = min(sqrt(rri**2 - min(rri, y2)**2), x2)
            rectarea = (x1 - prevx1) * (y2 - y1)
        if maxy1 <= y1:
            x2 = max(sqrt(rri**2 - min(rri, y1)**2), x1)
        #print '\tadjusted: x1=%f x2=%f rectarea=%f' % (x1, x2, rectarea)
        #print '\t          f(x1)=%f f(x2)=%f' % (sqrt(rri**2 - x1**2), sqrt(rri**2 - x2**2))
        #print '\t          A(x1)=%f A(x2)=%f' % (areaf(x1), areaf(x2))
        area = rectarea + (areaf(x2) - areaf(x1)) - (x2 - x1) * y1
        #print '=> returning %f' % area
        return area

    gaparea = 0.0
    x1 = r + f
    x2 = r + g - f
    for i in xrange(1000):
        #print 'part', i, gaparea
        if x1 > rri: break
        y1 = r + f
        y2 = r + g - f
        for j in xrange(1000):
            areapart = area(x1, y1, x2, y2)
            if areapart == 0.0 or y1 > rri: break
            gaparea += areapart
            y1 += 2*r + g
            y2 += 2*r + g
        x1 += 2*r + g
        x2 += 2*r + g

    return 1.0 - gaparea * 4 / pi / rr**2

import sys
next = iter(sys.stdin).next
ncases = int(next())
for i in xrange(ncases):
    f, rr, t, r, g = map(float, next().split())
    prob = process(f, rr, t, r, g)
    print 'Case #%d: %.10f' % (i+1, prob)
    sys.stdout.flush()
    #if i==2: break

