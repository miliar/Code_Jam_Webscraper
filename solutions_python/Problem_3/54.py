#!/usr/bin/python

import mpmath
import math
import sys


def resolve(R,t,f,r,g):
    mpmath.mp.prec = 100
    pi = mpmath.pi

    if g<2*f:
        return "1"

    A = pi*R**2
    
    radio = R - t - f
    lado = (2*r+g)

    limite = int(radio/lado)

    for i in xrange(limite+2):

        a_x = i*lado + r + f
        b_x = i*lado + r + g - f
        for j in xrange(limite+1):
            a_y = j*lado + r + f
            b_y = j*lado + r + g - f

            A -= 4*intercept(a_x,a_y,b_x,b_y,radio)


    p = A / (pi*R**2)

    return "%.6f"%(p)

            

def intercept(a_x,a_y,b_x,b_y,radio):
    area = (b_x-a_x)*(b_y-a_y)
    radio2 =radio**2
    

    if radio2 < a_x**2 + a_y**2:
        return 0
    elif radio2 >= b_x**2 + b_y**2:
        return area
    else:
        if radio2 > a_x**2 + b_y**2:
            if radio2 > b_x**2 + a_y**2:
                #Case 1
                corte = (radio2 - b_y**2)**0.5
                return mpmath.quadts(lambda x: (radio2 - x**2)**0.5 ,corte,b_x) - (b_x-corte)*a_y + (b_y-a_y)*(corte-a_x)
            else:
                #Case 3
                return mpmath.quadts(lambda x: (radio2 - x**2)**0.5 ,a_y,b_y) - (b_y-a_y)*a_x
        else:
            if radio2 > b_x**2 + a_y**2:
                #Case 2
                return mpmath.quadts(lambda x: (radio2 - x**2)**0.5 ,a_x,b_x) - (b_x-a_x)*a_y
            else:
                #Case 4
                corte = (radio2 - a_y**2)**0.5
                return mpmath.quadts(lambda x: (radio2 - x**2)**0.5 ,a_x,corte) - (corte-a_x)*a_y

def read_in():
    mpmath.mp.prec = 100
    fd = open("in")

    n = int(fd.readline())
    out=[]

    for i in xrange(n):
        print "Create: %d       \r"%(i),
        sys.stdout.flush()
        
        line = fd.readline()[:-1].split(" ")
        f = mpmath.mpf(line[0])
        R = mpmath.mpf(line[1])
        t = mpmath.mpf(line[2])
        r = mpmath.mpf(line[3])
        g = mpmath.mpf(line[4])
        
        out.append("Case #%d: %s"%(i+1,resolve(R,t,f,r,g)))

    return "\n".join(out)



print read_in()

