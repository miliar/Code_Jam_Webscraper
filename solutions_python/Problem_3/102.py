from __future__ import division
import psyco
psyco.full()
from sys import stdout

from math import *

class read_in:
    def __init__(self,fn):
        self.it=open(fn)
    def next(self):
        return self.it.next().strip()
       
def dist( x0,y0,x1,y1):
    return sqrt( (x1-x0)**2 + (y1-y0)**2 )

def dist2( x,y):
    return  x*x + y*y
       
def find_p1(x0,x1,y0,y1,r):
    y = sqrt(r*r -x0*x0)
    if y >= y0 and y < y1:
        return (x0,y),"l"
    x = sqrt(r*r-y1*y1)
    if x >= x0 and x < x1:
        return (x,y1),"u"
    assert(0)
        
def find_p2(x0,x1,y0,y1,r):
    x = sqrt(r*r-y0*y0)
    if x >= x0 and x < x1:
        return (x,y0),"d"
    y = sqrt(r*r -x1*x1)
    if y >= y0 and y < y1:
        return (x1,y),"r"
    assert(0)
    
def angle(p1,p2):
    a1 = asin( p1[1]/ sqrt(dist2(*p1) ) )
    a2 = asin( p2[1]/ sqrt(dist2(*p2) ) )
    if p1[0] < 0 :
        a1 = pi - a1;
    if p2[0] < 0 :
        a2 = pi - a2;
    return a2-a1;

def find_area(x0,y0,x1,y1,Rt):
    p1,d1 = find_p1(x0,x1,y0,y1,Rt)
    p2,d2 = find_p2(x0,x1,y0,y1,Rt)
    a = abs(angle(p1,p2))
    Ss = 0.5*Rt*Rt*(a-sin(a))
    assert (Ss >= 0)
    d = d1+d2
    k = x1-x0
    S = 0
    if d == "lr":
        a = p1[1] - y0
        b = p2[1] - y0
        assert (a>b)
        assert (a>0)
        assert (b>0)
        assert (a<k)
        assert (b<k)
        S = b*k + k*(a-b)/2 + Ss
    elif d == "ld":
        a = p1[1] - y0
        b = p2[0] - x0
        assert (a>0)
        assert (b>0)
        assert (a<k)
        assert (b<k)
        S = a*b/2 + Ss
    elif d == "ur":
        a = x1- p1[0]
        b = y1-p2[1]
        assert (a>0)
        assert (b>0)
        assert (a<k)
        assert (b<k)
        S = k*k - a*b/2 + Ss
    elif d == "ud":
        a = p1[0] - x0
        b = p2[0] - x0
        assert (a>0)
        assert (b>0)
        assert (a<k)
        assert (b<k)
        S = a*k + (b-a)*k/2 + Ss
    else:
        assert (0)
    return S
    
   
def check(f, R, t, r, g ):
    x=0
    y=0
    Rt = R - t
    A = 0
    AC = (pi* R * R ) / 4
    count = 0
    while x < R:
        y = 0
        while y < R:
            count += 1
            x0 = x + r + f
            y0 = y + r + f
            x1 = x0 + g - 2*f
            y1 = y0 + g - 2*f
            
            if dist (0,0, x0,y0) > Rt-f \
                    or x0 >= x1 \
                    or y0 >= y1 :
                break
            if dist( 0,0, x1,y1) < Rt-f:
                A += (g-2*f)**2
            else:
                a = find_area(x0,y0,x1,y1,Rt-f)
                A += a
            y = y + 2*r + g
        x = x + 2*r + g
    return 1 - (A/AC)
       
if __name__ == "__main__":
    it = read_in("C-large.in")
    N = int(it.next())
    for n in range(N):
        f, R, t, r, g = map(float,it.next().split())
        p = check(f, R, t, r, g )
        print "Case #%d: %f" %(n+1,p)
        stdout.flush()
           
           
      
  

  