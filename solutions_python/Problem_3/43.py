#!/usr/bin/env python
#-*- coding:utf-8 -*-

import psyco; psyco.full()

from math import *

def approx1(r, l, L):
    return  1.0 - (l ** 2 / L ** 2)

def in_circle(r, a):
    if sqrt(a[0] ** 2 + a[1] ** 2) <= r:
        return True

def in_circle_non_inclusive(r, a):
    if sqrt(a[0] ** 2 + a[1] ** 2) < r:
        return True

def integral(x1, x2):
    return (asin(x2) + x2*sqrt(1 - x2**2))/2 - (asin(x1) + x1*sqrt(1 - x1**2))/2

def cut_square_area(r, p1, p2, rectangle_area):
    x1, y1 = p1
    x2, y2 = p2
    a = r**2 * integral(x1/r, x2/r)
    a = a - (x2-x1) * y2
    area = rectangle_area + a
    return area


def approx2(r, l, L):
    n = int(r/L) + 1
    area = 0
    border = (L-l)/2
    
    for i in range(n):
        for j in range(n):
            a = i * L + border, j * L + border
            #b = a[0] + l, a[1]
            x, y = c = i * L + border + l, j * L + border + l
            x, y = min(r, x), min(r, y)
            #d = a[0], a[1] + l
            
            if in_circle(r, c):
                area += l ** 2
            
            elif in_circle_non_inclusive(r, a):
                
                px1 = sqrt(r**2 - y**2)
                if a[0] > px1:
                    p1 = a[0], sqrt(r**2 - a[0]**2)
                else:
                    p1 = px1, y
                    
                
                py2 = sqrt(r**2 - x**2)
                if a[1] > py2:
                    p2 = sqrt(r**2 - a[1]**2), a[1]
                else:
                    p2 = x, py2
                
                rectangle_area = (p2[0]-p1[0]) * (p2[1]-a[1]) + \
                                 (p1[0]-a[0]) * (p1[1]-a[1])
                
                #print i, j
                #print a, c
                #print p1, p2
                
                aa = cut_square_area(r, p1, p2, rectangle_area)
                
                #print aa
                #print
                
                area += aa
    
    return 1 - 4*(area) / (pi * r ** 2)

def proba(r, R, l, L):
    if r < 0 or l < 0:
        return 1
    
    approx = approx2(r, l, L)
    return (r**2 * approx + R**2 - r**2) / (R**2)

def test():
    print approx2(1000., 0.3, 0.5)

if __name__ == '__main__':
    from sys import argv, exit
    if len(argv) < 2:
        test()
        exit()
    
    file_name = argv[1]
    lines = open(file_name).read().split('\n')[0:-1]
    nb_inputs = int(lines[0])
    line_no = 0
    lines = lines[1:]
    
    for n in range(nb_inputs):
        line = lines[line_no]
        f, R, t, r, g = map(float, line.split(' '))
        line_no += 1
        print 'Case #%s: %.6f' % (n+1, proba(R - t - f, R, g - 2*f, g + 2*r)) 

