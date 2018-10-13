
##            
## PROBLEM SOLVING ALGORITHM 
##  
def solve(a,b,k):
    ## brute force solution (not for large dataset)
    ret = 0
    for i in range(a):
        for j in range(b):
            if (i&j)<k:
                ret += 1

    return ret
                    
##            
## MAIN LOOP: read(from stdin) - solve - print(to stdout) 
##
T = int(input())
for t in range(T):
    
    ## read case
    a,b,k = [int(item) for item in input().rstrip().split()]
        
    ## solve and print result
    result = solve(a,b,k)
    print('Case #'+str(t+1)+': '+str(result))
