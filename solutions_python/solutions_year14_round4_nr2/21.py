
##            
## PROBLEM SOLVING ALGORITHM 
##  
def solve(n,a):
    swaps = 0
    
    a2 = list(a)
    a2.sort()

    ## check elements in sorted order
    ## test 'swapping out to left or right hand side'
    for item in a2:
        pos = a.index(item)
        swaps += min(pos,len(a)-pos-1)
        a.remove(item)
        
    return swaps
                    
##            
## MAIN LOOP: read(from stdin) - solve - print(to stdout) 
##
T = int(input())
for t in range(T):
    
    ## read case
    n = int(input())
    a = [int(item) for item in input().rstrip().split()]
        
    ## solve and print result
    result = solve(n,a)
    print('Case #'+str(t+1)+': '+str(result))
