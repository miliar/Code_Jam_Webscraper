INPUT_FILE = 'inputs/C-large.in'
OUTPUT_FILE = 'outputs/C-large.out'

f_in = open(INPUT_FILE, 'r')
f_out = open(OUTPUT_FILE, 'w+')

T = int(f_in.readline())
for t in range(T):
    R, k, N = [int(i) for i in f_in.readline().split()]
    groups = [int(i) for i in f_in.readline().split()]
    totalDeficit = 0      
    
    # startGroupIndex -> resulting deficitCache for kEff
    deficitCache = []
    # startGroupIndex -> first group for the next roller coasters run
    nextGroupCache = []
    # fill the caches for every group
    for group in range(len(groups)):
        currSum = 0
        currGroup = group
        groupNumber = 0
        while ((currSum + groups[currGroup] <= k) and (groupNumber < N)):
            currSum += groups[currGroup]
            currGroup = (currGroup + 1) % len(groups) # clever overflow handling
            groupNumber += 1
            
        deficitCache.append(k - currSum)
        nextGroupCache.append(currGroup)
        
    metaIndexCache = []
    metaDeficitCache = []
    currGroup = 0
    r = 0
    while (r < R):
        metaIndexCache.append(currGroup)
        
        currDeficit = deficitCache[currGroup]
        metaDeficitCache.append(currDeficit)
        totalDeficit += currDeficit
        
        currGroup = nextGroupCache[currGroup]
        r += 1
        if (currGroup in metaIndexCache):
            indexInMetaCache = metaIndexCache.index(currGroup)
            cycleDefict = sum(metaDeficitCache[indexInMetaCache:])
            cycleLength = len(metaIndexCache) - indexInMetaCache
            
            numberOfCycles = (R - r) // cycleLength
            totalDeficit += cycleDefict * numberOfCycles
            r += numberOfCycles * cycleLength
            currCacheIndex = indexInMetaCache
            while(r < R):
                totalDeficit += metaDeficitCache[currCacheIndex]
                r += 1;
                currCacheIndex = (currCacheIndex + 1) % len(metaIndexCache)
                
            break
    
    strRes = "Case #" + str(t + 1) + ": " + str(R * k - totalDeficit)
    f_out.write(strRes + "\n")
    print(strRes)
    
f_in.close()
f_out.close() 
