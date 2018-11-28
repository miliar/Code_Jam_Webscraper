from math import *

def root1(a, b, c):
    return (-b+sqrt(pow(b, 2.0)-4.0*a*c))/(2.0*a)

def root2(a, b, c):
    return (-b-sqrt(pow(b, 2.0)-4.0*a*c))/(2.0*a)

def f(n, r, t):
    return 2.0*pow(n, 2)+(2.0*r-1.0)*n-t

T = int(input())
for test in range(0, T):
    s = raw_input()
    sl = s.split()
    r = int(sl[0])
    t = int(sl[1])
    r1 = root1(2, 2*r-1, -t)
    r2 = root2(2, 2*r-1, -t)
    res = int(floor(max(r1, r2)))
    print "Case #%s:" % str(test+1),
    if (f(res,r,t) <= 0):
        print res
    else:
        print res-1
    

    
