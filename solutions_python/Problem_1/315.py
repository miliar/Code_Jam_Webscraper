inFile = open("A-large.in", "r")
outFile = open("A-large.out", "w")

cases = int(inFile.readline())

for caseNum in range(cases):

    engines = []
    queries = []

    numEngines = int(inFile.readline())
    for i in range(numEngines):
        engines.append(inFile.readline().rstrip())



    numQueries = int(inFile.readline())
    for i in range(numQueries):
        queries.append(inFile.readline().rstrip())



    engineSet = set()
    switchCount = 0

    for i in range(numQueries):
        nextQuery = queries[i]
        engineSet.add(nextQuery)
        if len(engineSet) == numEngines:
            switchCount = switchCount + 1
            engineSet = set()
            engineSet.add(nextQuery)


    

    outString = "Case #" + str(caseNum + 1) + ": " + str(switchCount) + "\n"
    print outString.rstrip()
    
    outFile.write(outString)
    
            





inFile.close()
outFile.close()
