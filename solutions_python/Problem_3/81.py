#! /usr/bin/python
# -* coding:utf-8 -*-

import sys
import math
from decimal import * 
input=sys.stdin.read()
inList=input.split('\n')
N=int(inList.pop(0))

def makelist( R, t, r, g ):
    cur = 0.
    ret = []
    num = 0
    while 1:
        cur = num*(g+2*r)
        ret.append([cur+r+f,cur+g+r-f])
        if cur > R+t:
            break
        num+=1
    return ret


def abs( v ):
    if v > 0:
        return v
    return -v

def rest2( x1,y1,x2,y2, R ):
    rad = math.acos( (x1*x2+y1*y2)/(R*R))
    ret = R*R*rad/2
    ret -= abs(x1*y2-x2*y1)/2.
    return ret

def calS1( l, x1,y1, x2,y2, sx1, sy1, sx2, sy2,  R ):
    ret = l*(y1-sy1+x2-sx1)/2.
    ret += abs((x1-sx1)*(y2-sy1)-(x2-sx1)*(y1-sy1))/2.
    ret += rest2( x1,y1,x2,y2, R )
    return ret

def calS2( l, x1,y1, x2,y2, sx1, sy1, sx2, sy2,  R ):
    ret = l*(x1-sx1+x2-sx1)/2.
    ret += rest2( x1,y1,x2,y2, R )
    return ret

def calS3( l, x1,y1, x2,y2, sx1, sy1, sx2, sy2,  R ):
    ret = l*(y1-sy1+y2-sy1)/2.
    ret += rest2( x1,y1,x2,y2, R )
    return ret

def calS4( l, x1,y1, x2,y2, sx1, sy1, sx2, sy2,  R ):
    ret = (y1-sy1)*(x2-sx1)/2.
    ret += rest2( x1,y1,x2,y2, R )
    return ret

def rest( x, y, l, R ):
    xp = []

    if R - x[0] >= 0:
        yy = math.sqrt( R*R - x[0]*x[0] )
        xp.append( [x[0],yy,0] )
    if R - x[1] >= 0:
        yy = math.sqrt( R*R - x[1]*x[1] )
        xp.append( [x[1],yy,1] )
    if R - y[0] >= 0:
        xx = math.sqrt( R*R - y[0]*y[0] )
        xp.append( [xx,y[0],2] )
    if R - y[1] >= 0:
        xx = math.sqrt( R*R - y[1]*y[1] )
        xp.append( [xx,y[1],3] )

    xp2 = []
    flag = []
    for tmpx,tmpy,i in xp:
        if x[0] <= tmpx <= x[1] and y[0] <= tmpy <= y[1]:
            xp2.append( [tmpx,tmpy] )
            flag.append(i)

    x1,y1 = xp2[0]
    x2,y2 = xp2[1]
    if flag == [ 1, 3]:
        return calS1( l, x1,y1, x2,y2, x[0],y[0],x[1],y[1], R )
    elif flag == [ 2, 3]:
        return calS2( l, x1,y1, x2,y2, x[0],y[0],x[1],y[1], R )
    elif flag == [ 0, 1]:
        return calS3( l, x1,y1, x2,y2, x[0],y[0],x[1],y[1], R )
    elif flag == [ 0, 2]:
        return calS4( l, x1,y1, x2,y2, x[0],y[0],x[1],y[1], R )
    return 0

def prb(f,R,t,r,g):
    all = math.pi*(R)*(R)/4.
    xlist = makelist( R-t, t, r, g )
    hit = 0.
    for y in xlist:
        for x in xlist:
            if x[1]*x[1] + y[1]*y[1] < (R-f-t)*(R-f-t):
                hit += (g-2*f)*(g-2*f)
            elif x[0]*x[0] + y[0]*y[0] < (R-f-t)*(R-f-t):
                hit += rest( x, y, g-2*f, R-f-t )

    return 1. - hit/all




for i in range(N):
    f,R,t,r,g = inList.pop(0).split()
    f = float(f)
    R = float(R)
    t = float(t)
    r = float(r)
    g = float(g)
    print "Case #%d: %f"%(i+1,prb(f,R,t,r,g))

    
