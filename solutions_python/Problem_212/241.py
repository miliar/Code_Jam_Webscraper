
from collections import defaultdict
from math import ceil

def solve(g, p, sizes):
    if p == 2:
        even = 0
        odd = 0
        for s in sizes:
            if s % 2 == 0:
                even += 1
            else: 
                odd += 1
        return even + ceil(odd / 2.0)
    if p == 3:
        mod3 = [0, 0, 0]

        for s in sizes:
            mod3[s % 3] += 1

        ans = mod3[0]

        pairs = min(mod3[1], mod3[2])
        mod3[1] -= pairs
        mod3[2] -= pairs
        
        ans += pairs

        if mod3[1] > 0:
        
            ans += ceil(mod3[1] / 3.0)
        if mod3[2] > 0:
            ans += ceil(mod3[2] / 3.0)
        return ans




for i in xrange(input()):
    g, p = map(int, raw_input().split(' '))
    sizes = map(int, raw_input().split(' '))
    ans = solve(g, p, sizes)


    print "Case #%d: %d" % (i+1, ans)