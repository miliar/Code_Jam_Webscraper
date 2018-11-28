def solve(a, mo, curcost, maxcost, ix, molen):
    if ix >= molen:
        return curcost
    
    if a > mo[ix] :
        #maxcost -= 1
        #print "absorbed " , a, ix, mo[ix]
        curcost = solve(a+mo[ix], mo, curcost, maxcost, ix+1, molen)
    else:
        if curcost < maxcost:
            #insert
            cost1 = solve(a*2 -1, mo, curcost+1, maxcost, ix, molen)
            #delete
            cost2 = solve(a, mo, curcost+1, maxcost, ix+1, molen)
            #print "c1, c2", cost1, cost2, a, ix
            curcost = min(cost1,cost2)
        
    return curcost

t = int(raw_input())
for i in xrange(t):
    a,n = map(int, raw_input().split())
    mo = map(int, raw_input().split())
    mo.sort()
    #print mo
    res = solve(a, mo, 0, n, 0, n)
    print "Case #%s: %s" % (i+1, res)
    
