#!/usr/bin/python

import sys

def comp(a, b):
    
    return(a[1] - b[1])
    
def sortDict(adict):
    items = adict.items()
    items.sort(comp)    
    
    return [key for key, value in items]

def GetBestSearchEngine(engineNames, queries, currIndex):
    
    list = queries[currIndex:]
    maxDist = 0
    chosenName = ''
    for engineName in engineNames:
        
        try:
            dist = list.index(engineName)
        except:
            return(engineNames.index(engineName))
        
        if dist >= maxDist:
            maxDist = dist
            chosenName = engineName        

    return(engineNames.index(chosenName))
    
'''
def GetBestSearchEngine(engineNames, index, queries):
    
    if index >= len(queries):
        return(-1)
    
    sortQueries = sortDict(CountQueries(engineNames, queries[index:]))
    
    currQuery = queries[index]
    nextQuery = ''
    if index+1 < len(queries):
        nextQuery = queries[index+1]
    
    if nextQuery != '':
        x1 = 0    
        while (sortQueries[x1] == queries[index]) and (sortQueries[x1] == nextQuery):
            x1 += 1         
    else:
        x1 = 0    
        while (sortQueries[x1] == queries[index]):
            x1 += 1         

    x2 = GetBestSearchEngine(engineNames, index+1, queries)
    
    chosen = x1
    if x2 < x1:
        chosen = x2        
    
    if x2 < 0:
        chosen = x1
        
    return(chosen)

def CountQueries(engineNames, queryList):
    
    searchQueriesDict = {}
    
    for engine in engineNames:
        searchQueriesDict[engine] = 0
    
    for query in queryList:
        searchQueriesDict[query] = searchQueriesDict[query] + 1
                
    return(searchQueriesDict)
'''

def main():
    
    caseCount = int(sys.stdin.readline().strip())
    
    for caseNum in xrange(1, caseCount+1):
        
        searchEngineCount = int(sys.stdin.readline().strip())

        searchQueriesDict = {}
        
        searchEngineNames = []
        for searchEngine in xrange(searchEngineCount):
            engine = sys.stdin.readline().strip()
            searchEngineNames.append(engine)            
        
        searchQueriesCount = int(sys.stdin.readline().strip())
        
        searchQueries = []
        for searchQuery in xrange(searchQueriesCount):
            query = sys.stdin.readline().strip()
            searchQueries.append(query)
                
        switchCount = 0
        if len(searchQueries) > 0:
            searchEngineIndex = GetBestSearchEngine(searchEngineNames, searchQueries, 0)
            #print searchEngineIndex
            
        for index, searchQuery in enumerate(searchQueries):            
            
            if searchEngineNames[searchEngineIndex] == searchQuery:                            
                
                searchEngineIndex = GetBestSearchEngine(searchEngineNames, searchQueries, index)
    
                switchCount += 1              
                
        
        print 'Case #%d: %d' % (caseNum, switchCount)
    
main()