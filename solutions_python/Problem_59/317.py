#!/usr/bin/python
# 2010 Round1A
''' Usage %s
'''
import logging

CurrentDebugLevel=logging.DEBUG

def ProcessCase(inFile, caseNum):
    logging.debug('Case %d', caseNum)
    param = inFile.readline().strip().split()
    logging.debug(param)
    existDirCnt = int(param[0])
    createDirCnt = int(param[1])
    
    existDir = {'':{}}
    for i in range(existDirCnt):
        pathList = inFile.readline().strip().split('/')
        curLevel = existDir
        for name in pathList:
            if name not in curLevel: curLevel[name] = {}
            curLevel = curLevel[name]
    count = 0
    for i in range(createDirCnt):
        pathList = inFile.readline().strip().split('/')
        curLevel = existDir
        for name in pathList:
            if name not in curLevel: 
                curLevel[name] = {}
                count += 1
            curLevel = curLevel[name]
        
    result = [count]
    
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
    question = 'A'
    dataSet = 2
    attemptCount = 0   
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