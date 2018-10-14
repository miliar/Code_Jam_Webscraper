#!/usr/bin/python

import logging

CurrentDebugLevel=logging.DEBUG

#engineNameList = []
#queryRequestList = []

def ProcessQueries(engineNum, queryNum, engineNameList, queryRequestList):
    switchNum = 0
    logging.debug('E=%d Q=%d', engineNum, queryNum)
    #logging.debug(engineNameList)
    #logging.debug(queryRequestList)
    querySet = set()
    for query in queryRequestList:
        querySet.add(query)
        if len(querySet) == engineNum:
            querySet.clear()
            querySet.add(query)
            switchNum += 1
    return switchNum 

def OutputResult(caseNum, outFile, switchNum):
    outFile.write('Case #%d: %d\n' % (caseNum, switchNum))

def ProcessDataFile(fileName):
    inFile = open(fileName, 'r')
    line = inFile.readline()
    lineCount = int(line)
    
    engineNameList = dict()#[]
    queryRequestList = []
    outFile = open(fileName + '.out.txt', 'w')
    for i in xrange(1, lineCount + 1):
        line = inFile.readline()
        engineNum = int(line)
        for j in xrange(engineNum):
            line = inFile.readline()
            engineNameList[line.strip()] = 0 #.append(line.strip())
            
        line = inFile.readline()
        queryNum = int(line)
        for j in xrange(queryNum):
            line = inFile.readline()
            queryRequestList.append(line.strip())
        logging.debug('Case %d', i)
        switchNum = ProcessQueries(engineNum, queryNum, engineNameList, queryRequestList)
        engineNameList.clear()# = []
        queryRequestList = []
        logging.debug('Case #%d: %d' % (i, switchNum))
        OutputResult(i, outFile, switchNum)
    outFile.close()

def main():
    logging.basicConfig(level=CurrentDebugLevel, datefmt='%Y.%m.%d %H:%M:%S', format='%(asctime)s %(levelname)-5s %(message)s')
    
    #ProcessDataFile('A-small.txt')
    #ProcessDataFile('A-small-attempt2.in')
    ProcessDataFile('A-large.in')

if __name__ == '__main__': main()