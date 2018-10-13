import math

T = int(raw_input())

for tt in range(T):
    r, t = [int(i) for i in raw_input().split()]
    
    limit = t
    
    res = 0
    sqrt_delta = math.sqrt((2*r-1)**2 + 8*t)
    x1 = (2*r-1 - sqrt_delta)/(-4)
    x2 = (2*r-1 + sqrt_delta)/(-4)
    print 'Case #%s: %s' % (tt+1, int(math.floor(x1)-max(1, math.ceil(x2)) + 1))