import math

def dami(n, k):
    if n % 2 == 1:
        rl = (n/2, n/2)
    else:
        rl = ((n/2), (n/2)-1)
    if k == 1:
        return rl
    if k % 2 == 1:
        return dami(rl[1], int(k/2))
    else:
        return dami(rl[0], int(k/2))
t = int(raw_input())

for case in range(1, t+1):
    [n, k] = map(int, raw_input().split())
    (r,l) = dami(n, k)
    
    print "Case #%s: %s %s" % (case, r, l)
        


