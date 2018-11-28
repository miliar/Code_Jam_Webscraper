def route(engineList, searchList):
    def isProblematic(searchBool):
        return len([False for searchItem in searchBool if searchItem == False]) == 0

    #def findProblematic(searchBool):
    #    return [searchIndx for (searchItem,searchIndx) in zip(searchBool,range(0,len(searchBool))) if searchItem == False][0]

    def restProblematic():
        return [False for index in range(0,len(engineList))]
    
    def doProblematic(boolSearch,engineList,searchItem):
        l1 = [engineIndx for (engineItem,engineIndx) in zip(engineList,range(0,len(engineList))) if searchItem.find(engineItem) != -1]
        l2 = boolSearch

        for index in l1:
            l2[index] = True

        return l2
    
    boolSearch = restProblematic()
    currSwitch = 0

    for searchItem in searchList:
        boolSearch = doProblematic(boolSearch,engineList,searchItem)

        if isProblematic(boolSearch):
            currSwitch = currSwitch + 1            
            boolSearch = restProblematic()
            boolSearch = doProblematic(boolSearch,engineList,searchItem)

    return currSwitch

def intfs(path):    
    ifile = open(path,'r').read().split('\n')
    ofile = open('out.out2','w')

    tseek = 0
    times = int(ifile[tseek])

    results = []

    for index in range(0,times):
        engineSize = int(ifile[tseek + 1])
        engineList = [str(ifile[tseek + 2 + index]) for index in range(0,engineSize)]

        tseek = tseek + 1 + engineSize

        searchSize = int(ifile[tseek + 1])
        searchList = [str(ifile[tseek + 2 + index]) for index in range(0,searchSize)]

        tseek = tseek + 1 + searchSize

        results.append(route(engineList,searchList))

    for (item,index) in zip(results,range(1,len(results) + 1)):
        ofile.write('Case #' + str(index) + ': ' + str(item) + '\n')

    ofile.flush

    return results

    
