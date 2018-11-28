'''
Created on May 8, 2010

@author: AliJ
'''

def parse_num():
    return map(int, raw_input().split())

def process_case():
    (R,k,N)=parse_num()
    groupSizes = parse_num()
    endGroups=[0]*N
    rideSizes=[0]*N
    
    currentGroupSize=0
    currentGroup=0
    while currentGroup < N and currentGroupSize+groupSizes[currentGroup] <= k:
        currentGroupSize += groupSizes[currentGroup]
        currentGroup+=1
    
    endGroups[0]=currentGroup%N
    rideSizes[0]=currentGroupSize
        
    for i in range(1,N):
        currentGroupSize -= groupSizes[i-1]
        currentGroup%=N
        
        if currentGroup == i:
            currentGroupSize = groupSizes[currentGroup]
            currentGroup +=1
            currentGroup %=N
        
        while currentGroup != i and currentGroupSize+groupSizes[currentGroup] <= k:
            currentGroupSize += groupSizes[currentGroup]
            currentGroup+=1
            currentGroup %=N
            
        endGroups[i]=currentGroup%N
        rideSizes[i]=currentGroupSize
    
    groupStarted = [False]*N
    whenStarted = [-1]*N
    profitSoFar=[0]*N
    
    groupStarted[0]=True
    whenStarted[0]=0       
    currentGroup = endGroups[0]
    profitSoFar[0]=rideSizes[0]
    ridesTaken = 1
    
    while ridesTaken < R and groupStarted[currentGroup]==False:
        groupStarted[currentGroup]=True
        whenStarted[currentGroup]=ridesTaken
        profitSoFar[ridesTaken]=profitSoFar[ridesTaken-1]+rideSizes[currentGroup]
        currentGroup = endGroups[currentGroup]
        ridesTaken+=1
        
    if ridesTaken==R:
        return profitSoFar[ridesTaken-1]
    
    
    cycleLength=ridesTaken-whenStarted[currentGroup]

    
    if currentGroup==0:
        cycleProfit= profitSoFar[ridesTaken-1]
    else:
        cycleProfit=profitSoFar[ridesTaken-1]-profitSoFar[whenStarted[currentGroup]-1]
        
    
    money=profitSoFar[ridesTaken-1]+cycleProfit*((R-ridesTaken)/cycleLength)
    
    ridesTaken= ridesTaken+ ((R-ridesTaken)/cycleLength)*cycleLength
    
    while ridesTaken < R:
        money+=rideSizes[currentGroup]
        currentGroup = endGroups[currentGroup]
        ridesTaken+=1
        
    return money
        

numCases = int(raw_input())



for i in range(numCases):
            
    print "Case #"+str(i+1)+":", (process_case())
