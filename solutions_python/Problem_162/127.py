import sys


##            
## MAIN LOOP: read(from stdin) - solve - print(to stdout) 
##


## create list
l = [None for _ in range(1000001)]
l[1] = 1
cache = [1]
n = 1
toFill = 999999
while toFill>0:
    n += 1
    nCache = []
    for item in cache:
        if item+1<=1000000 and l[item+1]==None and (item+1 not in nCache):
            nCache.append(item+1)
            l[item+1] = n
            toFill -= 1
        s = ""
        for ch in str(item):            
            s = ch+s
        if int(s)<=1000000 and l[int(s)]==None and (int(s) not in nCache):
            nCache.append(int(s))
            l[int(s)] = n
            toFill -= 1
    cache = nCache   
            
T = int(input())
for t in range(T):
    
    ## read case
    n = int(input())
        
    ## solve and print result
    result = l[n] #check(n)
    print('Case #'+str(t+1)+': '+str(result))

    ## progress output
    print('Done: '+str(t+1)+' of '+str(T), file=sys.stderr)
