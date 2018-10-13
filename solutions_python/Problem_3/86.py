import sys
from math import * 

def angle(a, b, r):
    if a*a + b*b >= r*r: return 0.0
    A = sqrt(r*r - a*a)
    B = sqrt(r*r - b*b)
    s = (A-b)*a / 2.0 + (B-a)*b / 2.0
    alpha = acos(a / r) - acos(B / r)

    cosa = (a*B + b*A) / r / r
    
    if (abs(acos(cosa) - alpha) > 1e-5):
        print acos(cosa), alpha


    res = r*r*(acos(cosa)) / 2 - s
    assert(res >= 0)
    #print res, r*r*pi
    return res

def main():
    N = int(sys.stdin.readline())
    for case in xrange(N):
        [f, R, t, r, g] = [float(x) for x in sys.stdin.readline().split()]
        #print f, R, t, r, g
        n  = int(ceil((R - t - r) / (g + 2*r))) + 10
        safe = 0.0
        if 2*f < g:
            for i in xrange(n):
                for j in xrange(n):
                    x = r + i * (g + 2*r)
                    y = r + j * (g + 2*r)
                    x1 = x + f
                    y1 = y + f
                    x2 = x + g - f
                    y2 = y + g - f
                    if x1*x1 + y1*y1 > (R-t)*(R-t):
                        continue
                    assert(x2 > x1)
                    assert(y2 > y1)
                    if x2*x2 + y2*y2 < (R-t)*(R-t):
                        safe += (g-2*f)*(g-2*f)
                    else:
                        #print angle(x1, y1, R-t) , angle(x2, y2, R-t) , angle(x2, y1, R-t) , angle(x1, y2, R-t)
                        delta = angle(x1, y1, R-t-f) + angle(x2, y2, R-t-f) - angle(x2, y1, R-t-f) - angle(x1, y2, R-t-f)
                        #if (delta > 0): print safe, delta
                        assert (delta <= (g-2*f)*(g-2*f) + 1e-5)

                        safe += delta

        safe *= 4
        total = R*R*pi
        print 'Case #%d: %.7f' % (case + 1, 1.0 - safe / total)
main()