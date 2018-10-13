def Greedy(listSearchEngines, listQueries, currSearch):
    firstPosDict = dict()
    for eachSE in listSearchEngines:
        try:
            firstFound = listQueries.index(eachSE)
            firstPosDict[eachSE] = firstFound
        except:
            return (eachSE, 0)
    maxValue = ['',0]
    for eachSE in firstPosDict:
        if firstPosDict[eachSE] > maxValue[1] and currSearch != eachSE:
            maxValue[1] = firstPosDict[eachSE]
            maxValue[0] = eachSE
    gotData, value = Greedy(listSearchEngines, listQueries[maxValue[1]:], maxValue[0])
    return maxValue[0], 1 + value
    
def dynaMin(listSearchEngines, listQueries, currSearch):
    firstPosDict = dict()
    solDict = dict()
    for eachSE in listSearchEngines:
        if eachSE == currSearch:
            continue
        try:
            firstFound = listQueries.index(eachSE)
            firstPosDict[eachSE] = firstFound
        except:
            return (eachSE, 0)
        solution, value = dynaMin(listSearchEngines, listQueries[firstFound+1:], eachSE)
        #print solution
        solDict[eachSE] = value
    minValue = ['',999999]
    for eachSE in solDict:
        if solDict[eachSE] < minValue[1] and currSearch != eachSE:
            minValue[1] = solDict[eachSE]
            minValue[0] = eachSE
    #print minValue
    #raw_input()
    #print minValue
    print 1 + minValue[1]
    return minValue[0], 1 + minValue[1]
        

if __name__ == '__main__':
    inFile = open('A-small-attempt2.in')
    inLines = inFile.readlines()
    inFile.close()
    numCases = int(inLines[0].strip())
    index = 1
    #print numCases
    for iCase in range(numCases):
        # index is case definition
        numSearchEngines = int(inLines[index])
        numQueries = int(inLines[index + numSearchEngines + 1])
        #print numSearchEngines
        #print numQueries
        ##
        listSearchEngines = [ se.strip() for se in (inLines[index + 1: index + 1 + numSearchEngines])]
        listQueries = [ queried.strip() for queried in \
                   (inLines[index + 2 + numSearchEngines: \
                            index + 2 + numSearchEngines + numQueries])]
        #print listSearchEngines
        #print listQueries
        countDict = dict()
        runningIndex = 0
        
        # Each Running Loop
        # Dynamic Programming
        #Initialize Values
        counting = -1
        value, counting = Greedy(listSearchEngines, listQueries, '')
        #print counting
#        for eachSE in listSearchEngines:
#            countDict[eachSE] = 0
#        for eachQuery in listQueries[runningIndex:]:
#            #Counting
#            countDict[eachQuery] += 1
#        # get min search engines
#        minValue = ['',999999]
#        for eachSE in countDict:
#            if countDict[eachSE] < minValue[1]:
#                minValue[1] = countDict[eachSE]
#                minValue[0] = eachSE
#        currentSE = minValue[0]
#        
#        counting = 0
#        for runningIndex in range(len(listQueries)):
#            if listQueries[runningIndex] != currentSE:
#                continue
#            counting += 1
#            for eachSE in listSearchEngines:
#                countDict[eachSE] = 0
#            for eachQuery in listQueries[runningIndex:]:
#                #Counting
#                countDict[eachQuery] += 1
#            # get min search engines
#            minValue = ['',999999]
#            for eachSE in countDict:
#                if countDict[eachSE] < minValue[1]:
#                    minValue[1] = countDict[eachSE]
#                    minValue[0] = eachSE
#            currentSE = minValue[0]
        #print counting
        print 'Case #%d: %d' % (iCase + 1, counting)        
        ##
        index += numSearchEngines + numQueries + 2
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        