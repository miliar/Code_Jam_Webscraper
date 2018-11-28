#!/usr/bin/env python

from sys import *
from math import *

def genCoord(r, g, R):
    yield r
    yield r + g
    c = r + g
    
    while c < R:
        yield c + 2*r
        c += 2*r
        yield c + g
        c += g
        
def distance(p1, p2):
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    
    return sqrt(dx*dx + dy*dy)

def getRects(r, g, f, R):
    xgen = genCoord(r, g, R)
    
    rects = []
    
    while True:
        try:
            x0 = xgen.next()
            x1 = xgen.next()
            
            ygen = genCoord(r, g, R)
            while True:
                try:
                    y1 = ygen.next()
                    y0 = ygen.next()
                        
                    dist = distance((0, 0), (x0, y1))                        
                    if dist < R:
                        rects.append(((x0, y0), (x1, y1)))
                except StopIteration:
                    break
        except StopIteration:
            break
        
    return rects

def sign(x):
    if x < 0:
        return -1
    else:
        return 1

def circleIntersect(r, p1, p2):
    (x1, y1, x2, y2) = (p1[0], p1[1], p2[0], p2[1])
    
    dx = x2 - x1
    dy = y2 - y1
    dr = sqrt(dx*dx + dy*dy)
    sqdr = dr*dr
    d = x1*y2 - x2*y1
    D = r*r*sqdr - d*d    
    
    if (D < 0):
        return False
    
    sqD = sqrt(D)
    
    x1 = (d*dy + sign(dy)*dx*sqD) / sqdr 
    y1 = (-d*dx + fabs(dy)*sqD) / sqdr
    x2 = (d*dy - sign(dy)*dx*sqD) / sqdr
    y2 = (-d*dx - fabs(dy)*sqD) / sqdr
    
    if x1 > 0 and y1 > 0:
        return (x1, y1)
    else:
        return (x2, y2)
    
def romberg(f, a, b, eps = 1E-8):
    R = [[0.5 * (b - a) * (f(a) + f(b))]]
    n = 1
    while True:
        h = float(b-a)/2**n
        R.append((n+1)*[None])
        R[n][0] = 0.5*R[n-1][0] + h*sum(f(a+(2*k-1)*h) for k in range(1, 2**(n-1)+1))
        for m in range(1, n+1):
            R[n][m] = R[n][m-1] + (R[n][m-1] - R[n-1][m-1]) / (4**m - 1)
        if abs(R[n][n-1] - R[n][n]) < eps:
            return R[n][n]
        n += 1
    
def safeArea(rect, f, R, t):
    (x0, y0) = rect[0]
    (x1, y1) = rect[1]
    dx = x1 - x0
    dy = y0 - y1
        
    if (dx < 2*f) or (dy < 2*f):
        return 0
    else:        
        sqArea = (y0 - y1 - 2*f) * (x1 - x0 - 2*f)
        if sqArea <= 0:
            return sqArea 
        
        (x2, y2) = ((x0 + f), (y0 - f))
        (x3, y3) = ((x1 - f), (y1 + f))
        if distance((0, 0), (x3, y2)) > R - t - f:
            r = R - t - f            
            p1 = circleIntersect(r, (x2, y2), (x2, y3))
            p2 = circleIntersect(r, (x2, y3), (x3, y3))
            if p2 == False or p2[0] > x3:
                p2 = circleIntersect(r, (x3, y2), (x3, y3))
                
            def func(x):
                p = circleIntersect(r, (x, y2), (x, y3))
                if p == False: return 0
                y = p[1]
                
                if y > y2:
                    return y2 - y3
                elif y < y3:
                    return 0
                else:
                    return y - y3
                
            trArea = romberg(func, x2, x3, 1E-12)
                
            return trArea
        else:
            return sqArea

def processCase(f, R, t, r, g, case):
    safe = 0
    rects = getRects(r, g, f, R - t)
    for r in rects:
        safe += safeArea(r, f, R, t) 
        
    unsafe = 0.25*pi*R*R
    if unsafe == 0:
        prob = 0
    else:
        prob = 1 - safe/unsafe
        
    print "Case #%d: %2.6f" % (case, prob)
    
    return

def process(lines):
    n = int (lines[0])
    case = 1
    i = 1
    while case <= n:
        (f, R, t, r, g) = lines[i].strip("\r\n").split(' ')
                
        processCase(float (f), float (R), float (t),
                    float (r), float (g), case)        
        
        case += 1
        i += 1
        

def usage():
    print "Usage %s input" % argv[0]

def main():    
    if len(argv) < 2:
        usage()
        exit()
        
    input = argv[1]
    f = open(input, 'r')
    
    try:
        lines = f.readlines()
        process(lines)
        
    finally:
        f.close()

if __name__ == '__main__':
    main()
    