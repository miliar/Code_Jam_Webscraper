def check(N,r,t):
    return (2*r+1+2*(N-1))*N<=t

def solve(r,t):
    ## use iteration algorithm
    n = 0
    while check(2**n,r,t):
        n += 1
    n -= 1
    if n==-1:
        return 0
    N = 0
    for i in range(n+1):
        if check(N+2**(n-i),r,t):
            N += 2**(n-i)
    return N
    
                    
##            
## MAIN PROGRAM
##
T = int(input())
for n in range(T):
    ## read case
    r,t = map(int, input().rstrip().split())
        
    ## solve and print result
    result = solve(r,t)
    print('Case #'+str(n+1)+': '+str(result))


   
 
