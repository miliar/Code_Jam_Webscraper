#!/usr/bin/env python

def findLongest(queries, start, engines, exclude):
    longestRun = -1
    longestEngine = ""
    for engine in engines:
        if engine != exclude:
            engineLength = 0
            for i in range(start, len(queries)):
                if engine != queries[i]:
                    engineLength += 1
                else:
                    break
            if engineLength > longestRun:
                longestRun = engineLength
                longestEngine = engine
    return longestEngine, start + longestRun + 1

def main():
    #Populate Structures#
    inFileName = "A-large.in"

    
    inFile = file(inFileName)
    
    cases = int(inFile.readline())
    #print "Cases: ", cases
    for case in range(0,cases):
        engines = []
        queries = []
        engineCount = int(inFile.readline())
        #print "Engines: ", engineCount
        for engineNum in range(0,engineCount):
            engine = str(inFile.readline()).strip()
            engines.append(engine)
            #print "Case ", case, " : Engine ", engineNum, " : ", engine

        queryCount = int(inFile.readline())
        #print "Queries: ", queryCount
        for queryNum in range(0,queryCount):
            query = str(inFile.readline()).strip()
            queries.append(query)
            #print "Case ", case, " : Query ", queryNum, " : ", query
        switches = 0
        
        #Begin Calculation#

        #print engines

        pivot = 0
        currentEngine = ""
        while pivot <= len(queries):
            oldpivot = pivot
            currentEngine, pivot = findLongest(queries, pivot, engines, currentEngine )
            #print "Chose", currentEngine, "Length: ", pivot - oldpivot, "Pivot: ", pivot
            switches += 1
        switches -= 1
        if(switches < 0):
            switches = 0
        print "Case #" + str(case +1)+ ": " + str(switches)
        #print "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"
main()
