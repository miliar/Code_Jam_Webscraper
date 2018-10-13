
##            
## PROBLEM SOLVING ALGORITHM 
##

## return character list and list with number of occurences
def parse(s):
    cList = [s[0]]
    nList = [1]
    
    for c in s[1:]:
        if c==cList[-1]:
            nList[-1] += 1
        else:
            cList.append(c)
            nList.append(1)
    return cList, nList
        
def solve(n,l):

    ## parse strings and check if character sequences are equal
    cList, nList = parse(l[0])
    nLists = [nList]
    for s in l[1:]:
        cList2,nList = parse(s)
        if cList2!=cList:
            return 'Fegla Won'
        nLists.append(nList)

    ## now compute number of actions
    ret = 0 
    for i in range(len(cList)):
        numList = [nLists[j][i] for j in range(n)]

        ## stupid test of modifications in the interval of occurrences
        mods = None
        for t in range(min(numList),max(numList)+1):
            m = sum([abs(item-t) for item in numList])
            if mods==None or m<mods:
                mods = m

        ret += mods

    return ret
                        
##            
## MAIN LOOP: read(from stdin) - solve - print(to stdout) 
##
T = int(input())
for t in range(T):
    
    ## read case
    n = int(input())
    l = [str(input().rstrip()) for _ in range(n)]
        
    ## solve and print result
    result = solve(n,l)
    print('Case #'+str(t+1)+': '+str(result))
