from math import pi
import math

def incircle(x, y, R):
    return x*x+y*y <= R*R

def seccoord(a, R):
    s = R*R-a*a
    if s <= 0:
        return 0
    return math.sqrt(s)

def handlesegment(x1, y1, x2, y2, R):
    a1 = math.atan2(y1, x1)
    a2 = math.atan2(y2, x2)
    a = abs(a1-a2)
    return 0.5*R*R*(a - math.sin(a))

def areasquare(x, y, g, R):

    if not incircle(x, y, R):
        return 0

    if g <= 0:
        return 0

    x2 = x + g
    y2 = y + g

    if incircle(x2, y2, R):
        return g*g

    tl_in = incircle(x, y2, R)
    br_in = incircle(x2, y, R)
    P = 0

    if tl_in:
        i1y = y2
        i1x = seccoord(y2, R)
        P += (i1x - x) * g
    else:
        i1x = x
        i1y = seccoord(x, R)


    if br_in:
        i2x = x2
        i2y = seccoord(x2, R)
        P += (i2y - y) * g
    else:
        i2y = y
        i2x = seccoord(y, R)

    if tl_in and br_in:
        P -= (i1x - x) * (i2y - y)

    P += (i1y - i2y) * (i2x - i1x) * 0.5
    P += handlesegment(i1x, i1y, i2x, i2y, R)

    return P

def handlesquare(x, y, g, R, f):
    return areasquare(x + f, y + f, g - 2*f, R - f)

def itersquares(R, r, g, f):
    x = r
    while x < R:
        y = r
        while y < R:
            yield handlesquare(x, y, g, R, f)
            y += g+2*r
        x += g+2*r



def run_case():
    f, R, t, r, g = (float(x) for x in input().split())
    
    P_tot = pi * R*R
    P_not = 0

    for P_tmp in itersquares(R-t, r, g, f):
        P_not += 4 * P_tmp

    return 1 - P_not / P_tot



def main():
    N = int(input())
    for i in range(N):
        r = run_case()
        print('Case #%d: %f' % (i+1, r))


main()
