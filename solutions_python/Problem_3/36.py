import sys
import math

sqrt = math.sqrt
atan2 = math.atan2

eps = 0.0000001


def sqminus(x,y):
    return sqrt(x*x-y*y)


def sqcirc(x1,y1,x2,y2,R):
#    print x1,y1,x2,y2,R
    odx = x2-x1
    ody = y2-y1

    if (x1*x1+y1*y1 > R*R):
        return 0
    if (x2*x2+y2*y2 < R*R):
        return (x2-x1)*(y2-y1)

    res = 0.0
    if (x1*x1+y2*y2 < R*R):
        xx = sqminus(R,y2)
        assert xx >= x1 - eps
        assert xx <= x2 + eps
        res += (xx-x1)*(y2-y1)
        x1 = xx
#        print "x1",x1

    if (x2*x2+y1*y1 < R*R):
        yy = sqminus(R,x2)
        assert yy >= y1 - eps
        assert yy <= y2 + eps
        res += (yy-y1)*(x2-x1)
        y1 = yy
#        print "y1",y1

    x2 = sqminus(R,y1)
    y2 = sqminus(R,x1)

    assert(abs(x1*x1+y2*y2-R*R) < eps)
    assert(abs(x2*x2+y1*y1-R*R) < eps)

    dangle = atan2(y1,x2)
    uangle = atan2(y2,x1)
    wedge = 0.5*R*R*(uangle-dangle)
    ltr = 0.5*y1*(x2 - (y1*x1/y2))
    utr = 0.5*(y2-y1)*(x1 - (y1*x1/y2))
    res += wedge - ltr - utr

#    print "res",res,odx*ody
    assert res >= 0 - eps
    assert res <= odx*ody+eps
    return res



def getline():
    return sys.stdin.readline()



def celych(r,g,x):
    return int((x+r)/(2*r+g))


def vdire(r,g,x):
    x -= celych(r,g,x)*(2*r+g)
    return (x > r and x < r+g)


def presah(r,g,x):
    return x - celych(r,g,x)*(2*r+g) - r

def rat(f,R,t,r,g):
    # process f
    t += f
    g -= 2*f
    r += f

    # effective radius for bounding holes
    rr = R - t

    dist = 2*r+g

    sum = 0

    if g <= 0 or t >= R:
        return 1.0

    cel = celych(r,g,rr)
    for li in range(cel):
        loy = r+li*dist
        upy = loy+g
        assert upy <= r+dist*cel
        upedge = sqminus(rr,upy)
        loedge = sqminus(rr,loy)

        licel = celych(r,g,upedge)
        lipart = celych(r,g,loedge) + 1

        linesum = g*g * licel
        for i in range(licel, lipart+1):
            linesum += sqcirc(r+i*dist, loy, r+i*dist+g, upy, rr)

        sum += linesum

    loy = r+cel*dist
    upy = loy+g
    if loy < rr:
        loedge = sqminus(rr,loy)
        lipart = celych(r,g,loedge) + 1
        linesum = 0
        for i in range(lipart+1):
            linesum += sqcirc(r+i*dist, loy, r+i*dist+g, upy, rr)

        sum += linesum

    return 1.0 - (sum*4.0/(math.pi*R*R))


def relirat(f,R,t,r,g):
    # process f
    t += f
    g -= 2*f
    r += f

    # effective radius for bounding holes
    rr = R - t

    dist = 2*r+g

    sum = 0

    kostek = celych(r,g,rr) + 3

    if g <= 0 or t >= R:
        return 1.0

    for j in xrange(kostek+1):
        for i in xrange(kostek+1):
            sum += sqcirc(r+i*dist,r+j*dist,r+i*dist+g,r+j*dist+g,rr)

    return 1.0 - (sum*4.0/(math.pi*R*R))

cases = int(getline())

for case in range(cases):
    [f,R,t,r,g] = [float(x) for x in getline().split()]
    print "Case #%d: %f" % (case + 1,rat(f,R,t,r,g))
#    print "%g" % (rat(f,R,t,r,g))
#    print "%f" % (relirat(f,R,t,r,g))

