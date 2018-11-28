#!/usr/bin/python

def paintable(r, mid, t):
    a = 2 * mid * (mid + 1)
    b = (mid + 1) * (2 * r + 1)
    return t >= (a + b)

paintable(1,1,10)

T = int(raw_input())
for x in range(T):
    lb = -1
    ub = 1 << 32
    lst = [int(s) for s in raw_input().split()]
    r = lst[0]
    t = lst[1]
    while(ub - lb > 1):
        mid = (lb + ub) / 2
        if(paintable(r,mid-1,t)):
            lb = mid
        else:
            ub = mid
    
    print "Case #" + str(x + 1) + ": " + str(lb)
