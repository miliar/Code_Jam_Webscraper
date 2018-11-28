from math import sqrt,pi,acos

import sys

def sq(x, y):
    return x*x + y*y
    
def other(rr, xy):
    return sqrt(rr-xy*xy)

# quarter-plane square-circle intersection area
def area(r, x0, y0, x1, y1):
    rr = r*r
    if(sq(x0, y0) > rr):
        return 0.0
    if(sq(x1, y1) < rr):
        return None
    if(sq(x0, y1) > rr):
        ax = x0
        ay = other(rr, ax)
    else:
        ay = y1
        ax = other(rr, ay)
    if(sq(x1, y0) > rr):
        by = y0
        bx = other(rr, by)
    else:
        bx = x1
        by = other(rr, bx)

    cc = sq(ax-bx, ay-by)
    dd = rr - cc/4
    d = sqrt(dd)
    arc = rr*acos(d/r)-d*sqrt(rr-dd)
    tri = (bx-ax)*(ay-by)/2
    left = (ax-x0)*(ay-by) 
    bottom = (bx-ax)*(by-y0) 
    center = (ax-x0)*(by-y0)
    return arc + tri + bottom + left + center

def holes(ring, r, g):
    if(g<=0.0):
        return 0.0
    a=0.0
    full=0
    for i in range(0, 30):
        x = (2*i+1)*r+g*i  
        if(x > ring): break  
        for j in range(0, 30):
            y = (2*j+1)*r+g*j
            if(y > ring): break  
            ta=area(ring, x, y, x+g, y+g)
            if(ta==None):
                full+=1
            else:
                a+=ta
    return a+full*g*g

for case in range(1, int(sys.stdin.readline())+1):
    ii = sys.stdin.readline().rstrip().split(' ')
    (f, bigr, t, r, g) = map(float, ii)
    total = pi*bigr*bigr
    ring = bigr-t
    
    # adjust to fly size
    ring -= f
    g-=2*f
    r+=f
    
    h = holes(ring, r, g)*4
    nohit = h/total
    
    print "Case #%d: %f" % (case, 1.0-nohit)
    