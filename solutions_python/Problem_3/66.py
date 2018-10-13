import sys
import math

def area_half(x0, r):
    if x0>0:
        return r*r*math.pi - area_half(-x0, r)
    asinx = x0/r
    if asinx<=-1.:
        return 0
    asinx = math.asin(asinx)
    return r*r*(asinx+math.pi/2+math.sin(2.*asinx)/2.)

def area(x0, y0, r):
    if x0>0:
        return area_half(y0, r) - area(-x0, y0, r)
    if y0>0:
        return area_half(x0, r) - area(x0, -y0, r)
    asinx = x0/r
    if asinx<=-1.:
        return 0
    asiny = y0/r
    if asiny<=-1.:
        return 0
    asinx = math.asin(asinx)
    asiny = math.asin(asiny)
    if asinx+asiny<-math.pi/2:
        return 0
    return x0*y0+ r*r*(math.sin(2*asinx)/4 + math.sin(2*asiny)/4 \
            + asinx/2 + asiny/2+math.pi/4)

def do_test(input):
    line = input.readline().split(' ')
    FLY = float(line[0])
    RAD = float(line[1])
    RING = float(line[2])
    STRING = float(line[3])
    SPACE = float(line[4])
    D =  2*STRING+SPACE
    n_str = int(math.ceil((RAD+STRING)/D))+3
     
    sum = 0.
    insideSq = 0

    bord_sq_min = RAD - RING - FLY-(SPACE/2.-FLY)*math.sqrt(2)
    bord_sq_min = bord_sq_min*bord_sq_min
    bord_sq_max = RAD - RING - FLY+(SPACE/2.-FLY)*math.sqrt(2)
    bord_sq_max = bord_sq_max*bord_sq_max
    eff_rad = RAD-RING-FLY
    if eff_rad<=0.:
        return 1.

    for x in range(-n_str-1, n_str+1):
        for y in range(-n_str-1, n_str+1):
            x1 = x*D+STRING
            x2 = (x+1)*D-STRING
            y1 = y*D+STRING
            y2 = (y+1)*D-STRING
            simple = True
            if x==-n_str-1:
                x1 = -RAD
                simple = False
            if x==n_str:
                x2 = RAD
                simple = False
            if y==-n_str-1:
                y1 = -RAD
                simple = False
            if y==n_str:
                y2 = RAD
                simple = False
            if simple:
                cx = (x1+x2)/2.
                cy = (y1+y2)/2.
                dist = cx*cx+cy*cy
                if dist<bord_sq_min:
                    insideSq += 1
                    continue
                if dist>bord_sq_max:
                    continue
            x1 += FLY
            y1 += FLY
            x2 -= FLY
            y2 -= FLY
            if x1>=x2: continue
            if y1>=y2: continue
            sum += area(x2, y2, eff_rad) - area(x1, y2, eff_rad) \
                    - area(x2, y1, eff_rad) + area(x1, y1, eff_rad)
    sum += insideSq*(SPACE - 2*FLY)*(SPACE - 2*FLY)
    sum /= math.pi*RAD*RAD
    return 1.-sum

input = sys.stdin

N = int(input.readline())

for test in range(N):
    answer = do_test(input)
    print 'Case #%(case)d: %(answer).8f' % \
        {'case': test+1, 'answer': answer}
