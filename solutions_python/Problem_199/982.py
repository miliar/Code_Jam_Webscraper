def solve(pcs, k):
    res = 0
    s = ""
    l = list(pcs)
    for i in range(len(pcs)):
        if l[i] == "+":
            continue
        for j in range (k):
            if (i + j >= len(pcs)):
                return "IMPOSSIBLE"
            else:
                if l[i + j] == "+":
                    l[i + j] = "-"
                else:
                    l[i + j] = "+"
        res += 1
        #print l
        
    return res
    
t=int(raw_input())
for cas in xrange(1,t+1):
    n=str(raw_input())
    arra = n.split()
    pcs = arra[0]
    k = int(arra[1])
    print "Case #{}: {}".format(cas,solve(pcs, k))
