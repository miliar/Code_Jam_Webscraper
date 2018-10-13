

##            
## PROBLEM SOLVING ALGORITHM 
##  
def solve(n,p,r,q):

    ## sort and determine min and max number of ratatouilles
    qs = []
    for i in range(n):
        l = q[i]
        l.sort()
        l2 = []
        for item in l:
            n_max = 110*item//(99*r[i])
            n_min = 90*item//(99*r[i])
            if (90*item) % (99*r[i]) > 0:
                n_min += 1
            if n_max >= n_min:
                l2.append((n_min,n_max))
        qs.append(l2)

    ## now start packaging
    kits = 0
    for (n_min,n_max) in qs[0]:
        indexList = []
        for i in range(1,n):
            index = None
            for j in range(len(qs[i])):
                (n_min2,n_max2) = qs[i][j]
                if n_max2>=n_min and n_min2<=n_max:
                    index = j
                    break
            indexList.append(index)
        if not None in indexList:
            for i in range(1,n):
                qs[i].remove(qs[i][indexList[i-1]])
            kits += 1
            
    return kits
                    
##            
## MAIN LOOP: read(from stdin) - solve - print(to stdout) 
##
T = int(input())
for t in range(T):
    
    ## read case
    n,p = [int(item) for item in input().rstrip().split()]
    r = [int(item) for item in input().rstrip().split()]
    q = [[int(item) for item in input().rstrip().split()]
         for _ in range(n)]
    
    ## solve and print result
    result = solve(n,p,r,q)
    print('Case #'+str(t+1)+': '+str(result))

    
