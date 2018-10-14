from codejam import *
from math import *

def dist(x1,y1,x2,y2):
    return sqrt((x1-x2)**2 + (y1-y2)**2)

def run(f):
    n=int(f.next())
    x=[]
    y=[]
    r=[]
    for i in range(n):
        xx,yy,rr = f.line(float)
        x.append(xx)
        y.append(yy)
        r.append(rr)

    if n==1:
        return r[0]
    elif n==2:
        return max(r[0],r[1])
    elif n==3:
        d=[
                max(dist(x[0],y[0],x[1],y[1])+r[0]+r[1],r[2]*2),
                max(dist(x[0],y[0],x[2],y[2])+r[0]+r[2],r[1]*2),
                max(dist(x[1],y[1],x[2],y[2])+r[1]+r[2],r[0]*2)]
        return min(d)/2
    return

def main(fn):
    f=Reader(fn)
    n=int(f.next())
    for i in range(n):
        print 'Case #%d:'%(i+1), '%.6f'%run(f)
    return

import sys
main(*sys.argv[1:])
