import sys

##            
## PROBLEM SOLVING ALGORITHM 
##  
def solve(r,c,n):
    # brute force algorithm: try all possibilities
    res = None
    for b in range(2**(r*c)):
        l = [int((1<<i)&b)!=0 for i in range(r*c)]

        # number of tenants must match
        if sum(l)==n:
            
            # check unhappiness
            uh = 0
            for row in range(r):
                for col in range(c-1):
                    if l[row*c+col]==1 and l[row*c+col+1]==1:
                        uh += 1
            for col in range(c):
                for row in range(r-1):
                    if l[row*c+col]==1 and l[(row+1)*c+col]==1:
                        uh += 1
            if res==None or uh<res:
                res = uh
    return res
    
                    
##            
## MAIN LOOP: read(from stdin) - solve - print(to stdout) 
##
T = int(input())
for t in range(T):
    
    ## read case
    r,c,n = [int(item) for item in input().rstrip().split()]
        
    ## solve and print result
    result = solve(r,c,n)
    print('Case #'+str(t+1)+': '+str(result))

    ## progress output
    print('Done: '+str(t+1)+' of '+str(T), file=sys.stderr)
