#!/usr/bin/python
# 2011 Qualification
''' Usage %s
'''
import logging

CurrentDebugLevel=logging.DEBUG

def ProcessCase(inFile, caseNum):
    logging.debug('Case %d', caseNum)
    param = inFile.readline().strip().split()
    #logging.debug(param)
    
    combineMap = {}
    opposedMap = {}
    elementSet = {}
    result = []
    
    combineCount = int(param[0])
    start = 1
    for i in range(combineCount):
        combine = param[start + i][:2]
        combineMap[combine] = param[start + i][2]
        combineMap[''.join(reversed(combine))] = param[1 + i][2]
        
    start += combineCount 
    opposedCount = int(param[start])
    start += 1
    for i in range(opposedCount):
        opposedMap[param[start + i][0]] = param[start + i][1]
        opposedMap[param[start + i][1]] = param[start + i][0]
    
    logging.debug(combineMap)
    logging.debug(opposedMap)
    start += opposedCount
    invokeCount = int(param[start])
    start += 1 
    invokeList = param[start]
    logging.debug(invokeList)

    for x in invokeList:
        if len(result) > 0:
            combine = result[-1] + x
        else:
            combine = x
        opposed = ''
        if x in opposedMap:     
            opposed = opposedMap[x]

        if combine in combineMap:
            last = result.pop()
            newElement = combineMap[combine]
            result.append(newElement)
            if last in elementSet: elementSet[last] -= 1
            if elementSet[last] <= 0: del elementSet[last]
            #elementSetnewElement)
        elif opposed in elementSet:
            elementSet.clear()
            result = []
        else:
            if x in elementSet: elementSet[x] += 1
            else: elementSet[x] = 1 
            result.append(x)
    
    return result

def OutputResult(outFile, caseNum, result):
    value = ', '.join(result)
    if len(result) == 0: value = ''
    outFile.write("Case #{}: [{}]\n".format(caseNum, value))
    logging.debug("Case #{}: [{}]\n".format(caseNum, value))

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
    question = 'B'
    dataSet = 1
    attemptCount = 2   
    isPractice = False
    
    partName = '-practice'
    dataSetNames = ['test', 'small', 'large']
    if dataSet == 0:
        dataFileName = '{0}-{1}.txt'.format(question, dataSetNames[dataSet])
    elif dataSet == 1:
        if not isPractice: partName = '-attempt{}'.format(attemptCount)
        dataFileName = '{0}-{1}{2}.in'.format(question, dataSetNames[dataSet], partName)
    else:
        if not isPractice: partName = ''
        dataFileName = '{0}-{1}{2}.in'.format(question, dataSetNames[dataSet], partName)

    ProcessDataFile(dataFileName)

if __name__ == '__main__': main()