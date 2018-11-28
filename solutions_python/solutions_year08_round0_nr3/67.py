
import sys

from math import asin, pi, sqrt

def f0(x, R):
    """ Half-circle parametrization """
    return sqrt(R*R - x*x)

def f1(x, R):
    """ Primitive of f0, divided by .5*R*R """
    x /= R
    return asin(x) + x * sqrt(1 - x*x)

def vert(x0, x1, y0, R):
    """ Area between x=x0, x=x1, y=y0 and circle """
    return .5*R*R *(f1(x1, R) - f1(x0, R)) - y0 * (x1 - x0)

def square(x0, y0, g, R):
    """ Area of a square part """
    x1 = x0 + g
    y1 = y0 + g
    x02 = x0*x0
    x12 = x1*x1
    y02 = y0*y0
    y12 = y1*y1
    R2 = R*R
    if x12 + y12 <= R2: #Complete square
        return g*g
    A = 0.
    if x12 + y02 > R2 and x02 + y12 > R2: #3 points out of the circle
        xi = f0(y0, R) #Intersection with the circle
        A = vert(x0, xi, y0, R)
    elif x12 + y02 <= R2 and x02 + y12 <= R2: #1 point out of the circle
        xi = f0(y1, R) #Intersection with the circle
        A = vert(xi, x1, y0, R) #Part with circular edge
        A += g * (xi - x0) #Rectangular part
    elif x12 + y02 > R2: #2 points out of the circle, case 1
        xi1 = f0(y1, R) #First intersection with the circle
        xi2 = f0(y0, R) #Second intersection with the circle
        A = vert(xi1, xi2, y0, R) #Part with circular edge
        A += g * (xi1 - x0) #Rectangular part
    else: #2 points out of the circle, case 2
        A = vert(x0, x1, y0, R)
    return A

def area(f, R, t, r, g):
    """ Area of the open part """
    rg = g - 2*f #Reduced gap
    if rg <= 0.:
        return 0.
    rR = R - t - f #Reduced inner radius
    if rR <= 0.:
        return 0.
    delta = g + 2*r
    x = r + f
    A = 0.
    while x < rR:
        ym = f0(x, rR)
        y = r + f
        while y < ym:
            A += square(x, y, rg, rR)
            y += delta
        x += delta
    return 4.*A

def prob(f, R, t, r, g):
    """ Probability """
    return 1. - (area(f, R, t, r, g) / (pi * R * R))

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print "Usage: %s <input> <output>" % sys.argv[0]
        sys.exit()
    fd = open(sys.argv[1], 'r')
    fd2 = open(sys.argv[2], 'w')
    n = int(fd.readline())
    for i in xrange(n):
        f, R, t, r, g = map(float, fd.readline().strip().split(' '))
        x = prob(f, R, t, r, g)
        fd2.write("Case #%i: %.6f\n" % (i + 1, x))
    fd.close()
    fd2.close()
