#!/usr/bin/python
from math import *

data = open('C-large.in','rt').read().splitlines()
N = int(data[0])
k = 1

res = ""

def func(R,x):
    try:
        return 1.0/2*x*sqrt(R**2-x**2)+1.0/2*R**2*atan(x/sqrt(R**2-x**2))
    except:
        return 1.0/2*x*sqrt(R**2-x**2)+1.0/2*R**2*pi/2

def per(R,x):
    return sqrt(R**2-x**2)

for i in xrange(N):
    f, R, t, r, g = map(float,data[k].split(' '))
    k+=1
    Rz = R-t-f
    Dl = 2*r+g
    s_count = int(Rz/Dl)+1
    x = s_count
    S = 0
    if g-2*f>0:
        for y in xrange(s_count):
            while (x>=0 and Rz<sqrt((Dl*x+r+f)**2+(Dl*y+r+f)**2)):
                x-=1
            if x<0:
                break
            while (x>=0 and Rz<sqrt((Dl*(x+1)-r-f)**2+(Dl*(y+1)-r-f)**2)):
                if Rz<sqrt((Dl*(x+1)-r-f)**2+(Dl*y+r+f)**2) and Rz<sqrt((Dl*x+r+f)**2+(Dl*(y+1)-r-f)**2):
                    p = per(Rz,Dl*y+r+f)
                    S+= func(Rz,p)-func(Rz,Dl*x+r+f)-(Dl*y+r+f)*(p-(Dl*x+r+f))
                elif Rz<sqrt((Dl*(x+1)-r-f)**2+(Dl*y+r+f)**2):
                    S+= func(Rz,Dl*(y+1)-r-f)-func(Rz,Dl*y+r+f)-(Dl*x+r+f)*(g-2*f)
                elif Rz<sqrt((Dl*x+r+f)**2+(Dl*(y+1)-r-f)**2):
                    S+= func(Rz,Dl*(x+1)-r-f)-func(Rz,Dl*x+r+f)-(Dl*y+r+f)*(g-2*f)
                else:
                    p = per(Rz,Dl*(y+1)-r-f)
                    S+= func(Rz,Dl*(x+1)-r-f)-func(Rz,p)-(Dl*y+r+f)*(Dl*(x+1)-r-f-p)+(g-2*f)*(p-(Dl*x+r+f))
                x-=1
            x+=1
            S+=x*(g-2*f)**2
        S = S*4
    else:
        S = 0
    res+="Case #%d: %0.7f\n" % (i+1,1-S/(pi*R**2))

open('C-large.out','wt').write(res)

