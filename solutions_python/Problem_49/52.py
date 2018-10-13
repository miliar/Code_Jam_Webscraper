from numpy import *

def leastRad(ps, rs):
    minCost = None
    for i in range(3):
        cost = leastDiam(ps, rs, i)
        if minCost is None or cost < minCost:
            minCost = cost
    minCost /= 2.0
    maxR = max(rs)
    if minCost < maxR:
        mincost = maxR
    return minCost

def sgnStar(x):
    if x < 0:
        return -1
    else:
        return 1

def leastDiam(ps, rs, i):
    j = 1 if i == 0 else 0
    k = 1 if i == 2 else 2
    pi = ps[i]
    ri = rs[i]
    pj = ps[j]
    rj = rs[j]
    pk = ps[k]
    rk = rs[k]
    dj = pj - pi
    dk = pk - pi
    djd = sqrt(dot(dj, dj))
    dkd = sqrt(dot(dk, dk))
    djdMax = djd + rj + ri
    djdMin = djd + rj - ri
    dkdMax = dkd + rk + ri
    dkdMin = dkd + rk - ri
    double = True
    mn = max(djdMin, dkdMin)
    mx = min(djdMax, dkdMax)
    return mx
        
        
infile = open("D-small-attempt1.in", "r")
outfile = open("out.out","w")
C = int(infile.readline())
for caseNo in xrange(1, C+1):
    N = int(infile.readline())
    xs = []
    ys = []
    rs = []
    for i in xrange(N):
        line = infile.readline()
        x, y, r = map(int, line.split())
        xs.append(x)
        ys.append(y)
        rs.append(r)
    xs = array(xs)
    ys = array(ys)
    rs = array(rs)
    ps = array([xs, ys]).transpose()
    if N < 3:
        rd = max(rs)
    else:
        rd = leastRad(ps, rs)
    rd = float(rd)
    print rd
    output = "Case #{0}: {1:.7f}\n".format(caseNo, rd);
    print output,
    outfile.write(output)
infile.close()
outfile.close()


        
            
        
    
