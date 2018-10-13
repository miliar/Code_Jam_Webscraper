def getNumOfSwitches(searchEngines, queries):
    currentSearchEngine = None
    switches = 0

    for i in range(len(queries)):
        if currentSearchEngine == None or currentSearchEngine == queries[i]:
            if currentSearchEngine != None:
                switches += 1

            # Make best switch
            maxLifeTime = None
            for searchEngine in searchEngines:
                lifeTime = 0
                for j in range(i, len(queries)):
                    if queries[j] == searchEngine:
                        break
                    lifeTime += 1
                if maxLifeTime == None or lifeTime >= maxLifeTime:
                    maxLifeTime = lifeTime
                    bestSwitch = searchEngine
            currentSearchEngine = bestSwitch

    return switches

mode = 0
caseCount = 0
case = 0

searchEngines = []
queries = []

numLeft = 0

out = open("A-code.out", "w")
for line in open("A-large.in"):

    line = line.strip()
    
    if mode == 0:
        caseCount = int(line)
        mode = 1
        
    elif mode == 1:
        numLeft = int(line)
        if numLeft == 0:
            mode = 3
        else:
            mode = 2
        
    elif mode == 2:
        searchEngines.append(line)
        numLeft -= 1
        
        if numLeft == 0:
            mode = 3

    elif mode == 3:
        numLeft = int(line)
        if numLeft == 0:
            case += 1
            print 'Case #%i: %i' % (case, getNumOfSwitches(searchEngines, queries))
            out.write('Case #%i: %i' % (case, getNumOfSwitches(searchEngines, queries)) + '\n')
            searchEngines = []
            queries = []
            mode = 1

            if caseCount == case:
                break
        else:
            mode = 4

    elif mode == 4:
        queries.append(line)
        numLeft -= 1

        if numLeft == 0:
            case += 1
            print 'Case #%i: %i' % (case, getNumOfSwitches(searchEngines, queries))
            out.write('Case #%i: %i' % (case, getNumOfSwitches(searchEngines, queries)) + '\n')
            searchEngines = []
            queries = []
            mode = 1

            if caseCount == case:
                break

out.close()
