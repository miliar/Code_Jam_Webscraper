##            
## PROBLEM SOLVING ALGORITHM 
##  
def solve(n,k):

    # hashtable for counting empty stalls (in row)
    l = {n:1}
    
    while True:
        m = max(l)
        rs = (m-1)//2
        ls = m-1-rs
        n = l.pop(m)
        if n>=k:
            return str(max(ls,rs))+" "+str(min(ls,rs))
        
        for item in [ls,rs]:
            if item in l:
                l[item] += n
            else:
                l[item] = n
        k -= n
                    
##            
## MAIN LOOP: read(from stdin) - solve - print(to stdout) 
##
for t in range(int(input())):
    
    ## read case
    n,k = [int(item) for item in input().rstrip().split()]
        
    ## solve and print result
    result = solve(n,k)
    print('Case #'+str(t+1)+': '+str(result))
