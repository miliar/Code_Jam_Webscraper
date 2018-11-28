import itertools

##            
## PROBLEM SOLVING ALGORITHM 
##

## small dataset can be solved by trying it out
def solve(n,m,zips,flights):

    ## create list of flights
    fList = [[] for _ in range(n)]
    for x,y in flights:
        fList[x-1].append(y-1)
        fList[y-1].append(x-1)
    
    ret = None

    ## test all permutations (small dataset only...)
    for travel in itertools.permutations(list(range(n))):

        ## check whether flight booking is possible
        history = [travel[0]]
        for i in range(1,n):
            while history!=[]:
                ## can append next city?
                if travel[i] in fList[history[-1]]:
                    history.append(travel[i])
                    break
                else:
                    ## if not: return flight now
                    history.pop()
                    

        if history!=[]:
            
            # travel possible -> compute value
            v = 0
            for city in travel:
                v = 100000*v + zips[city]
            if ret==None or v<ret:
                ret =v
            
    return ret
                    
##            
## MAIN LOOP: read(from stdin) - solve - print(to stdout) 
##
T = int(input())
for t in range(T):
    
    ## read case
    n,m = [int(item) for item in input().rstrip().split()]
    zips = [int(input().rstrip()) for _ in range(n)]
    flights = [[int(item) for item in input().rstrip().split()] for _ in range(m)]
    
    ## solve and print result
    result = solve(n,m,zips,flights)
    print('Case #'+str(t+1)+': '+str(result))

