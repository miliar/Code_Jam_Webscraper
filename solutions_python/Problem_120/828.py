import sys
import math

def read():
    return sys.stdin.readline()

def format(tup):
    return 'Case #%d: %d'%tup

def draw(r, t):
    area = 2*r + 1
    num = 1
    while area <= t:
        num += 1
        r += 2    
        area += 2*r + 1 
    num -= 1
    return num 

def draw2(r, t):
    num = (math.sqrt(8.0*t + (2.0*r - 1.0)**2) \
        - (2.0*r - 1.0))/4.0
    if 2.0*num*num + (2.0*r-1.0)*num > t:
        return int(num -1) 
    else: 
        return int(num)

for i in xrange(int(read())):
    r, t = map(int,read().split()) 
    print format((i+1,draw(r,t)))

