import sys

## stupid try of all possibilities --- won't work on large set
def sim(E,R,N,l,e,n):
    if n==N:
        return 0
    ret = 0
    for spend in range(max(0,e-E+R),e+1):
        r = sim(E,R,N,l,e-spend+R,n+1)+spend*l[n]
        if r>ret:
            ret = r
    return ret
    

def solve(E,R,N,l):
    if R>E:
        R=E
    return sim(E,R,N,l,E,0)
                    
##            
## MAIN PROGRAM
##
T = int(input())
for t in range(T):
    ## read case
    E,R,N = map(int, input().rstrip().split())
    l = list(map(int, input().rstrip().split()))
        
    ## solve and print result
    result = solve(E,R,N,l)
    print('Case #'+str(t+1)+': '+str(result))

    ##progress output
    print('Done: '+str(t+1)+' of '+str(T), file=sys.stderr)

