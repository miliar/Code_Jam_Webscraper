from math import floor

def minN(c, f, x):
    return (x*f-c*f-2*c)/(c*f)

def tot(c,f,x,n):
    s = 0
    for i in xrange(n,0,-1):
        s += 1.0/((i-1)*f+2)
    return c*s + x/(n*f+2)

keis = int(raw_input())
for kei in xrange(keis):
    c, f, x = [float(y) for y in raw_input().split()]
    o = 'Case #%d: %.7f'
    if x < c:
        print o % (kei+1, x/2.0,)
    else:
        n = floor(minN(c,f,x))+1
        if n < 0:
            n = 0
        print o % (kei+1, tot(c,f,x,int(n)),)
