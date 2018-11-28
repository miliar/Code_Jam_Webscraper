import math

nt = int(input())

def solve(n,k):
    #print "solve n = ",n, " k = ",k    
    if k == 1:        
        d1 = (n-1)/2
        d2 = (n-1) - d1
        return min(d1,d2), max(d1,d2)
    
    te = k-1        
    if (n-1)%2 == 0:
        ns = (n-1)/2
        #right mimic left
        if te%2 == 0:
            #last person in right
            return solve(ns, te/2)
        else:
            return solve(ns, (te+1)/2)
    else:
        #left mimic right
        ns = n - n/2
        if te%2 == 0:
            return solve(ns-1, te/2)
        else:
            return solve(ns,(te+1)/2)
            
for it in xrange(nt):    
    n,k = map(int, raw_input().split())    
    resp = solve(n,k)    
    print "Case #{}: {} {}".format(it+1, resp[1],resp[0])