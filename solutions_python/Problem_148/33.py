
##            
## PROBLEM SOLVING ALGORITHM 
##  
def solve(n,x,s):
    s.sort()

    discs = 0

    while s!=[]:
        discs += 1
        
        # put biggest file on disc
        remainingSize = x - s.pop()
        # check if another file can be put on same disc
        # choose it as big as possible
        aFiles = [item for item in s if item<=remainingSize]
        if aFiles!=[]:
            s.remove(aFiles[-1])
    
    return discs
    
                    
##            
## MAIN LOOP: read(from stdin) - solve - print(to stdout) 
##
T = int(input())
for t in range(T):
    
    ## read case
    n,x = [int(item) for item in input().rstrip().split()]
    s = [int(item) for item in input().rstrip().split()]
        
    ## solve and print result
    result = solve(n,x,s)
    print('Case #'+str(t+1)+': '+str(result))
