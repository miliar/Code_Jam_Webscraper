#!/usr/bin/python
# 2011 Qualification
''' Usage %s
'''
import logging

CurrentDebugLevel=logging.DEBUG

def ProcessCase(inFile, caseNum):
    logging.debug('Case %d', caseNum)
    param = inFile.readline().strip().split()
    logging.debug(param)
    
    # position of each robot
    currentPos = {'O' : 1, 'B' : 1}
    
    count = int(param[0])
    lastBot = 'B'
    usedTime = 0
    
    totalTime = 0
    for i in range(count):
        currentBot = param[1 + i * 2]
        nextButton = int(param[2 + i * 2])
        curPos = currentPos[currentBot]
        currentPos[currentBot] = nextButton
        needTime = abs(nextButton - curPos)
        totalTime += 1 # push the button

        if currentBot != lastBot:
            lastBot = currentBot # change bot and reset time
            if needTime > usedTime: 
                totalTime += (needTime - usedTime)
                usedTime = 1 + (needTime - usedTime)
            else: usedTime = 1
        else:
            usedTime += needTime + 1 # +1 for push button
            totalTime += needTime
                
        
    result = [totalTime]
    
    return result

def OutputResult(outFile, caseNum, result):
    value = result[0]
    outFile.write("Case #{}: {}\n".format(caseNum, value))
    logging.debug("Case #{}: {}\n".format(caseNum, value))

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