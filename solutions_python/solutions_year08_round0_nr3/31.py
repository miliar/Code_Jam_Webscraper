#fly swatter
from math import *

def height(a, x):
    return sqrt(a*a - x*x)
    
def strips(R, r, g):
    yield 0.0, r
    x = r + g
    while x < R:
        yield x, x+2*r
        x += 2*r + g
    
def column(a, x1, x2):   
    integral = lambda x,u: 0.5*(x*u + a*a*asin(x/a))
    u = lambda x: sqrt(a*a - x*x)
    x2 = min(a, x2)    
    return integral(x2, u(x2)) - integral(x1, u(x1))

def cmp_strip(R, r, g):   
    if r<=0 or R<=0:
        return 0.0
    if g<=0:
        return pi * R*R
    A = 0.0
    for x1, x2 in strips(R, r, g):
        A += column(R, x1, x2)
    return 4 * A
    
def cmp_gaps(R, r, g):
    if r<=0 or R<=0:
        return 0.0
    if g<=0:
        return pi * R*R
    A = 0.0
    ngaps = 0
    for x, x2 in strips(R, r, g):
        #sum gaps from bottom to top
        for y, y2 in strips(R, r, g):
            ngaps += 1
            #upper right
            if x2*x2+y2*y2 < R*R:
                A += (y2-y)*(x2-x)
                continue
            #lower left
            if x*x+y*y >= R*R:
                break
            #lower right
            if x2*x2+y*y > R*R:
                #place lower right in
                x2 = height(R, y)
            if x*x+y2*y2 >= R*R:
                #upper left is out
                A += column(R, x, x2) - y*(x2-x)
                break
            #only upper right is out
            new_x2 = height(R, y2)
            A += column(R, new_x2, x2) - y*(x2-new_x2) + (y2-y)*(new_x2-x)
            x2 = new_x2
    print ngaps
    return 4 * A

def solve(f, R, t, r, g):
    sure = pi * R*R
    ref = r + f
    gap = g - 2*f    
    Rinner = R - t - f
    Aring = pi * (R*R - Rinner*Rinner)
    Astrips = cmp_strip(Rinner, ref, gap)
    Agaps = cmp_gaps(Rinner, ref, gap)
    Aswatter = Aring + 2*Astrips - Agaps
    print 'sure', sure
    print 'ring', Aring
    print 'strips', Astrips
    print 'gaps', Agaps
    return Aswatter / sure

#loading input
fin = open('C-large.in')
fout = open('output.txt','w')
N = int(fin.readline())
for en in xrange(N):
    #read data
    data = fin.readline().split()
    data = map(lambda x: float(x), data)
    f, R, t, r, g = data
    p = solve(f, R, t, r, g)
    print p
    fout.write( 'Case #%d: %.7f\n' % (en+1, p) )
fin.close()
fout.close()
    
    
