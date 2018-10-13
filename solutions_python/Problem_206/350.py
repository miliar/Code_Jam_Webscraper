numCases = int(raw_input())

for t in range(1, numCases+1):
    d, n = [int(s) for s in raw_input().split()]
    k = []
    s = []
    for i in range(n):
        ki, si = [int(r) for r in raw_input().split()]
        k.append(ki)
        s.append(si)

    print "Case #{}: {}".format(t, d/max([(float(d-ki)/si) for ki,si in zip(k,s)]))