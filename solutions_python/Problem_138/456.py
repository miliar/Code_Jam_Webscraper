

## Ken's strategy:
##
##   - if I can make the point, use the lightest block which will
##     make the point (function returns True)
##   - otherwise give away the lightest block (return False)
##
def playKen(mTold, blocks):
    l = [i for i in range(len(blocks)) if blocks[i]>mTold]
    if l!=[]:
        blocks.pop(l[0])
        return True
    blocks.pop(0)
    return False

##            
## SIMULATE GAMES 
##    
def solve(naomiBlocks, kenBlocks):

    naomiBlocks.sort()
    kenBlocks.sort()
    
    ## simulate deceitful war game
    ##
    ## Noaomi's strategy:
    ##
    ## process sorted list starting with minimum weight
    ##
    ## - if Ken's lightest block is lighter than processing block,
    ##   get the point by telling him a weight higher than his heaviest block
    ##   to force him to give away his lightest block
    ## - otherwise tell a weight slightly below his heaviest block, so Ken
    ##   will use his heaviest block to get the point (but loose the
    ##   heaviest block)
    ##
    kB = list(kenBlocks)
    deceitfulPoints = 0
    for m in naomiBlocks:
        if kB[0]<m:
            kB.pop(0)
            deceitfulPoints += 1
        else:
            kB.pop(-1)
            
    ## simulate (fair) war game
    ##
    ## Naomi's strategy: use sorted list starting with heaviest block
    ##
    warPoints = 0
    for mTold in naomiBlocks:
        if not playKen(mTold, kenBlocks):
            warPoints += 1
    
    return str(deceitfulPoints)+" "+str(warPoints)


##            
## MAIN LOOP: read(from stdin) - solve - print(to stdout) 
##
T = int(input())
for t in range(T):
    
    ## read case
    input()
    naomiBlocks = [float(item) for item in input().rstrip().split()]
    kenBlocks = [float(item) for item in input().rstrip().split()]
        
    ## solve and print result
    result = solve(naomiBlocks, kenBlocks)
    print('Case #'+str(t+1)+': '+str(result))
