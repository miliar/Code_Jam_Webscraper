from heapq import *
def f(line):
    Ns, Ks = line.split(' ')
    N = int(Ns)
    K = int(Ks)
    keys = [-N]
    values = {N: 1}
    while K>0:
        gap = -heappop(keys)
        amount = values[gap]
        remain2 = (gap-1)/2
        remain1 = gap-remain2-1
        for r in (remain1,remain2):
            if r in values:
                values[r] += amount
            else:
                values[r] = amount
                heappush(keys, -r)
        K -= amount
        values[gap] = 0
        # print remain1, remain2
    return " ".join(map(str,(remain1, remain2)))
        
    
T = int(raw_input())
for i in xrange(1,T+1):
    print "Case #%d: %s" % (i, f((raw_input())))
    
    # 5
    # 0
    # 1
    # 2
    # 11
    # 1692Square Brackets [ ] | English Club