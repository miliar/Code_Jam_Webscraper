cases = int(raw_input())

for i in xrange(cases):
    R, k, N = (int(x) for x in raw_input().split())
    g = [int(x) for x in raw_input().split()]
    total = 0
    for j in xrange(R):
        p = 0
        group = []
        while g and p+g[0] <= k:
            p += g[0]
            group.append(g.pop(0))
        total += p
        g.extend(group)
    print "Case #%i: %i" % ( i+1, total)
        
