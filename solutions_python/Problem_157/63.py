import sys

##            
## PROBLEM SOLVING ALGORITHM 
##  
def solve(x,l):
    table = [[(0,False),(1,False),(2,False),(3,False)],
             [(1,False),(0, True),(3,False),(2, True)],
             [(2,False),(3, True),(0, True),(1,False)],
             [(3,False),(2,False),(1, True),(0, True)]]

    ## algorithm for small dataset only
    s = x*l

    ## try to find solution in string by parsing

    # start with '1'
    v = 0
    vSign = False
    
    state = "find_i"
    
    for ch in s:
        # quaternion algebra
        i = "1ijk".index(ch)
        v, sign = table[v][i]
        vSign ^= sign

        if state=="find_i":
            if v==1 and vSign==False:
                v = 0
                state = "find_j"
                
        elif state=="find_j":
            if v==2 and vSign==False:
                v = 0
                state = "parse_to_end"
        
    if state=="parse_to_end" and v==3 and vSign==False:
        return "YES"
    else:
        return "NO"
        
    print('debug: '+str(l))
                    
##            
## MAIN LOOP: read(from stdin) - solve - print(to stdout) 
##
T = int(input())
for t in range(T):
    
    ## read case
    _,x = [int(item) for item in input().rstrip().split()]
    l = input().rstrip()
    
    ## solve and print result
    result = solve(x,l)
    print('Case #'+str(t+1)+': '+str(result))

    ## progress output
    print('Done: '+str(t+1)+' of '+str(T), file=sys.stderr)
