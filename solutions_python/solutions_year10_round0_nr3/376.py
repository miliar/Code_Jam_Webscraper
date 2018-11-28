#!/usr/bin/python
# 2010 Qualification
''' Usage %s
'''
import logging

CurrentDebugLevel=logging.DEBUG

def CalculateTotalEarning(earnList, repeatStart, runNum):
    total = 0
    nonRepeatTotal = 0
    repeatTotal = 0
    
    repeatAt = -1
    for i, p in enumerate(earnList):
        if p[0] == repeatStart:
            repeatAt = i
            break
        nonRepeatTotal += p[1]

    if repeatAt >= 0: # the rest run will repeat the same sequence from repeatStart
        for i in range(repeatAt, len(earnList)):
            repeatTotal += earnList[i][1]
        total += repeatTotal
    if runNum > 0: # if we need more than one repeat those runs in earnList
        repeatLen = len(earnList) - repeatAt # there are how many runs in repeat area
        if repeatLen > 0:
            total += (int(runNum / repeatLen) * repeatTotal)
            runNum %= repeatLen
        for i in range(repeatAt, repeatAt + runNum):
            total += earnList[i][1]
    return total + nonRepeatTotal

def VerifyCase2(runNum, capacity, groupList):
    total = 0
    while runNum > 0:
        earnSum = 0
        isFull = False
        for i in range(start, len(groupList)):
            if earnSum + groupList[i] <= capacity:
                earnSum += groupList[i]
            else:
                start = i
                isFull = True
                break
        runNum -= 1

def VerifyCase(runNum, capacity, groupList):
    total = 0
    start = 0
    isOnceServe = False
    isFirst = True
    while runNum > 0:
        earnSum = 0
        isFull = False
        for i in range(start, len(groupList)):
            if earnSum + groupList[i] <= capacity:
                earnSum += groupList[i]
            else:
                start = i
                isFull = True
                break
        if isFirst:
            isFirst = False
            if start == 0: # we have very few guests to serve, so we can serve them once for all
                isOnceServe = True
                break
        if not isFull and earnSum < capacity: 
            start = 0 # start over
            for i in range(start, len(groupList)):
                if earnSum + groupList[i] <= capacity:
                    earnSum += groupList[i]
                else:
                    start = i
                    isFull = True
                    break
        elif not isFull:
            start = 0
            
        total += earnSum
        runNum -= 1
        
    if isOnceServe:
        total = sum(groupList) * runNum

    return total

def ProcessCase(inFile, caseNum):
    logging.debug('Case %d', caseNum)
    param = inFile.readline().strip().split()
    #logging.debug(param)
    groupList = [int(x) for x in inFile.readline().strip().split()]
    oldRunNum = runNum = int(param[0])
    capacity = int(param[1])
    
    startSet = set() # where it starts
    earnList = [] # start from which and earn how much
    
    start = 0
    isOnceServe = False
    isFirst = True
    while runNum > 0:
        startSet.add(start)
        earnSum = 0
        oldStart = start
        isChangedStart = False
        for i in range(start, len(groupList)):
            if earnSum + groupList[i] <= capacity:
                earnSum += groupList[i]
            else:
                start = i 
                isChangedStart = True
                break
        if isFirst:
            isFirst = False
            if start == 0: # we have very few guests to serve, so we can serve them once for all
                isOnceServe = True
                break
        if not isChangedStart and earnSum < capacity: 
            start = 0 # start over
            for i in range(start, len(groupList)):
                if earnSum + groupList[i] <= capacity:
                    earnSum += groupList[i]
                else:
                    start = i 
                    break
        elif not isChangedStart: start = 0 # start over
        earnList.append((oldStart, earnSum))
        runNum -= 1
        if start in startSet: break # we already done this before
    if isOnceServe:
        total = sum(groupList) * runNum
        #total = CalculateTotalEarning([(0, sum(groupList))], 0, runNum)
    else:
        total = CalculateTotalEarning(earnList, start, runNum)
        
#    realTotal = VerifyCase(oldRunNum, capacity, groupList)
#    if realTotal != total: 
#        logging.debug("Error Case #%d: %d != %d", caseNum, realTotal, total);
#        logging.debug("%d %d %d", oldRunNum, capacity, int(param[2]))
#        logging.debug(groupList)
    result = [total]
    
    return result

def OutputResult(outFile, caseNum, result):
    value = result[0]
    outFile.write("Case #{0}: {1}\n".format(caseNum, value))
    logging.debug("Case #{0}: {1}\n".format(caseNum, value))

def ProcessDataFile(fileName):
    inFile = open(fileName, 'r')
    line = inFile.readline()
    lineCount = int(line)
    outFile = open(fileName + '.out.txt', 'w')
    for i in range(1, lineCount + 1):
        result = ProcessCase(inFile, i)
        OutputResult(outFile, i, result)
    outFile.close()

def main():
    logging.basicConfig(level=CurrentDebugLevel, datefmt='%Y.%m.%d %H:%M:%S', format='%(asctime)s %(levelname)-5s %(message)s')
    question = 'C'
    #dataSet = 'small'
    dataSet = 'large'
    #dataSet = 'test'
    #attempt = '-attempt1'
    attempt = ''

    ProcessDataFile('{0}-{1}{2}.in'.format(question, dataSet, attempt))

if __name__ == '__main__': main()