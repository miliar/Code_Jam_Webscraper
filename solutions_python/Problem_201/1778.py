import time

def calculateLeft(inputArray, stallNo):
    leftDistance = 0
    for i in range(stallNo,0,-1):
        if(inputArray[i-1]==0):
            leftDistance = leftDistance + 1
        else:
            return leftDistance

def calculateRight(inputArray, stallNo, noStalls):
    rightDistance = 0
    for i in range(stallNo, noStalls+1): 
        if(inputArray[i+1]==0):
            rightDistance = rightDistance + 1
        else:
            return rightDistance
        
def getMinMaxToilet(noStalls, noPeople):
    outputArray = []    
    inputArray = [0]*(noStalls+2)
    inputArray[0] = 1
    inputArray[noStalls+1] = 1
    #print inputArray
    #print '________________________________________'
    for personId in range(1, noPeople+1):
        #print 'person : '+str(personId)
        minDict = {}
        maxDict = {}    
        for stallNo in range(1, noStalls+1):            
            #print 'stall : '+str(stallNo)
            if(inputArray[stallNo] ==0):
                Ls = calculateLeft(inputArray, stallNo)
                Rs = calculateRight(inputArray, stallNo, noStalls)
                minLsRs = min(Ls, Rs)
                maxLsRs = max(Ls, Rs)
                #print 'Ls '+str(Ls)+', Rs '+str(Rs)+', min '+str(minLsRs)+', max '+str(maxLsRs)
                minDict[stallNo] = minLsRs
                maxDict[stallNo] = maxLsRs
        #print minDict
        #print maxDict
        #print(max(minDict.values()))
        maxOfMinDict = max(minDict.values())
        stallToBeEntered = 0
        maxOfMaxDict = 0
        for i in sorted(minDict.keys(), reverse=True):
            if(minDict[i]==maxOfMinDict):
                if(maxDict[i]>=maxOfMaxDict):
                    stallToBeEntered = i
                    maxOfMaxDict = maxDict[i] 
        inputArray[stallToBeEntered] = 1
        #print maxOfMaxDict
        #print maxOfMinDict
        #print inputArray
        outputArray = [maxOfMaxDict, maxOfMinDict]
    return outputArray

def fileRead():
    start = time.time()
    fo = open("input.txt", "rw+")
    lineList = fo.readlines()
    noTestCases = int(lineList[0])
    f = open('output.txt', 'w')
    for i in range(1, noTestCases+1):
        inputStringList = lineList[i].split()
        N = int(inputStringList[0])
        K = int(inputStringList[1])
        result = getMinMaxToilet(N, K)
        print "Case #"+str(i)+": "+str(result[0])+" "+str(result[1])
        if(i==noTestCases):
            f.write("Case #"+str(i)+": "+str(result[0])+" "+str(result[1]))
        else:
            f.write("Case #"+str(i)+": "+str(result[0])+" "+str(result[1])+'\n')
    f.close()
    elapsed = (time.time() - start)
    print elapsed
    
def main():
    fileRead()

if __name__ == "__main__":
    main()