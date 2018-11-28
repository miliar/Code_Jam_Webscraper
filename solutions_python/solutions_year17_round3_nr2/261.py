def solve(ac, aj, ccs, dcs, cjs, djs):
    if ac + aj == 1:
        return 2

    if ac == 0:
        if min(cjs) + 720 >= max(djs):                        
            return 2
        if 1440 - max(cjs) + min(djs) <= 720:
            return 2
        return 4
            
    if aj == 0:
        if min(ccs) + 720 >= max(dcs):
            return 2
        if 1440 - max(ccs) + min(dcs) <= 720:
            return 2
        return 4
            
    return 2

t = int(raw_input())
for i in xrange(1, t + 1):
    ccs = []
    dcs = []
    cjs = []
    djs = []
    ac, aj = [int(x) for x in raw_input().split(" ")]
    for j in xrange(ac):
        c, d = [int(x) for x in raw_input().split(" ")]
        ccs.append(c)
        dcs.append(d)
    for j in xrange(aj):
        c, d = [int(x) for x in raw_input().split(" ")]
        cjs.append(c)
        djs.append(d)
    print "Case #{}: {}".format(i, solve(ac, aj, ccs, dcs, cjs, djs))
