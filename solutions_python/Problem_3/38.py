import sys
from math import *

def readline():
    return sys.stdin.readline()

def dist(x0, y0, x1, y1):
    return sqrt((x1-x0)**2 + (y1-y0)**2)

def arc(r, d):
    # r * sin(theta) = d/2
    theta = asin(d/2/r)
    a = r**2 * theta
    tri = r*cos(theta)*d/2
    return a - tri

#print arc(1, sqrt(2))

def main():
    ncase = int(readline())
    for case in range(ncase):
        f, R, t, r, g = map(float, readline().split())
        #if case + 1 != 1: continue
        #print 'f', f, 'R', R, 't', t, 'r', r, 'g', g

        x = 0
        y = 0
        #seen = set()
        area = pi * (R**2) / 4

        area_fullhole = max(0, g-2*f)**2
        area_miss = 0

        # sum fullhole
        yi = int(ceil(R / (2*r+g))) + 1
        xi = 0

        while True:
            x = xi*(2*r+g) + r
            if x >= R-t:
                break

            maxy = sqrt((R-t)**2 - x**2)
            while True:
                y = yi*(2*r+g) + r

                if yi < 0:
                    break
                if (x+g)**2 + (y+g)**2 <= (R-t)**2:
                    break
                yi -= 1


            yi += 1
            #for i in range(yi):
            #    seen.add((xi, i))
            area_x = max(0, yi)*area_fullhole
            area_miss += area_x
            xi += 1


        # sum partial hole
        yi = int(ceil(R / (2*r+g))) + 1
        xi = 0

        while True:
            x = xi*(2*r+g) + r
            if x >= R-t:
                break

            maxy = sqrt((R-t)**2 - x**2)
            while True:
                y = yi*(2*r+g) + r
                if y < maxy:
                    break
                yi -= 1

            #print 'xi, yi', xi, yi

            area_x = 0

            while True:
                y = yi*(2*r+g) + r

                x0 = x + f
                y0 = y + f
                x1 = x + g - f
                y1 = y + g - f
                if yi < 0:
                    break
                #print '*xi, yi', xi, yi
                if (x+g)**2 + (y+g)**2 <= (R-t)**2:
                    yi += 2
                    break
                #assert (xi, yi) not in seen
                #seen.add((xi, yi))
                yi -= 1
                #print (x0, y0), (x1, y1)
                if not x0 <= x1:
                    break
                assert x0 <= x1
                assert y0 <= y1
                assert 0 <= R-t-f


                if x0**2 + y0**2 < (R-t-f)**2:

                    if x1**2 + y0**2 < (R-t-f)**2:
                        if x0**2 + y1**2 < (R-t-f)**2:
                            # case A
                            #print 'A'
                            assert 0 <= R-t-f
                            if x1**2 + y1**2 > (R-t-f)**2:
                                x2 = sqrt((R-t-f)**2 - y1**2)
                                y2 = sqrt((R-t-f)**2 - x1**2)
                                a = area_fullhole - (x1-x2)*(y1-y2)/2 + arc(R-t-f, dist(x1, y2, x2, y1))
                                area_x += a
                            else:
                                pass
                                area_x += area_fullhole 
                        else:
                            # case B
                            #print 'B'
                            if x1**2 + y1**2 > (R-t-f)**2:
                                y2 = sqrt((R-t-f)**2 - x0**2)
                                y3 = sqrt((R-t-f)**2 - x1**2)

                                a = ((y2-y0) + (y3-y0)) * (x1-x0) / 2 + arc(R-t-f, dist(x0, y2, x1, y3))
                                area_x += a
                            else:
                                pass
                                area_x += area_fullhole 

                    else:
                        if x0**2 + y1**2 < (R-t-f)**2:
                            # case D
                            #print 'D'
                            x0, x1, y0, y1 = y0, y1, x0, x1
                            if x1**2 + y1**2 > (R-t-f)**2:
                                y2 = sqrt((R-t-f)**2 - x0**2)
                                y3 = sqrt((R-t-f)**2 - x1**2)

                                a = ((y2-y0) + (y3-y0)) * (x1-x0) / 2 + arc(R-t-f, dist(x0, y2, x1, y3))
                                area_x += a
                            else:
                                pass
                                area_x += area_fullhole 
                        else:
                            # case C
                            #print 'C'
                            if x1**2 + y1**2 > (R-t-f)**2:
                                x2 = sqrt((R-t-f)**2 - y0**2)
                                y2 = sqrt((R-t-f)**2 - x0**2)
                                a = (x2-x0)*(y2-y0)/2 + arc(R-t-f, dist(x0, y2, x2, y0))
                                area_x += a
                            else:
                                pass
                                area_x += area_fullhole 
            area_miss += area_x

            xi += 1


        #print 'area miss', area_miss, 'area', area
        print 'Case #%d: %.6f' % (case+1, 1.0 - area_miss/area)

main()
