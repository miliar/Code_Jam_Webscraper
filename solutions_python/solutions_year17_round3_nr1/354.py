import math, itertools

def compute(rhs):
    rmax = max(rhs)[0]
    area = math.pi * rmax * rmax
    for i in rhs:
        area = area + 2 * math.pi * i[0] * i[1]
    return area
        
def solve(n, k, rs, hs, rhs):
    rhs = sorted(rhs, key = lambda x: x[0]*x[1])

    best = 0
    for i in xrange(n-(k-1)):
        test = rhs[n-(k-1):n]
        test.append(rhs[i])        
        best = max(best, compute(test))
        
    return best

t = int(raw_input())
for i in xrange(1, t + 1):
    rs = []
    hs = []
    rhs = []
    n, k = [int(x) for x in raw_input().split(" ")]
    for j in xrange(n):
        r, h = [int(x) for x in raw_input().split(" ")]
        rs.append(r)
        hs.append(h)
        rhs.append((r, h))
    print "Case #{}: {}".format(i, solve(n, k, rs, hs, rhs))
