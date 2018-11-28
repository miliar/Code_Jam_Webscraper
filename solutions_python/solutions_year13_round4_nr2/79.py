import sys

## Brute force attack --- should work for small dataset

def mySort(l):
    r1 = []
    r2 = []
    for i in range(len(l)//2):
        if l[2*i]<l[2*i+1]:
            r1.append(l[2*i])
            r2.append(l[2*i+1])
        else:
            r1.append(l[2*i+1])
            r2.append(l[2*i])

    if len(r1)>1:
        return mySort(r1)+mySort(r2)
    else:
        return r1+r2

def solve(N,P):
    ## worst case 
    l = [i for i in range(2**N)]
    l2 = mySort(l)
    if P==len(l2):
        sol1 = 2**N-1
    else:
        sol1 = min(l2[P:])-1

    ## best case
    l.reverse()
    l2 = mySort(l)
    sol2 = max(l2[0:P])
    
    return str(sol1)+' '+str(sol2)
                    
##            
## MAIN PROGRAM
##
T = int(input())
for t in range(T):
    ## read case
    N,P = map(int, input().rstrip().split())
        
    ## solve and print results
    result = solve(N,P)
    print('Case #'+str(t+1)+': '+str(result))

    ##progress output
    print('Done: '+str(t+1)+' of '+str(T), file=sys.stderr)

    
