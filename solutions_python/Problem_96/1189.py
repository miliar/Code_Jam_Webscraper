#!/usr/bin/python
# 2012 Qualification
''' Usage %s
'''
import logging

CurrentDebugLevel=logging.DEBUG

def ProcessCase(inFile, caseNum):
    logging.debug('Case %d', caseNum)
    param = inFile.readline().strip().split()
    logging.debug(param)
    
    surprising = int(param[1])
    p = int(param[2])
    scores = [int(x) for x in param[3:]]
    
    # the least scores that had a best result of greater than or equal to p
    scoreWithoutSurprise = p * 3 - 2 # ex: 7 7 8
    if scoreWithoutSurprise < 0: scoreWithoutSurprise = p
    socreWithSurprise = p * 3 - 4  # ex: 6 6 8  
    if socreWithSurprise < 0: socreWithSurprise = p
    logging.debug("ScoreWithoutSurprise={}, SocreWithSurprise={}".format(scoreWithoutSurprise, socreWithSurprise))
    
    num = 0
    for s in scores:
        if s >= scoreWithoutSurprise: num += 1
        elif s >= socreWithSurprise and surprising > 0:
            num += 1
            surprising -= 1
    
    result = [num]
    
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
    question = 'B'
    dataSet = 2
    attemptCount = 0   
    isPractice = False
    hasLargeTest = False
    
    partName = '-practice'
    dataSetNames = ['test', 'small', 'large']
    if dataSet == 0:
        partName = ''
        if hasLargeTest: partName = '-Large'
        dataFileName = '{0}-{1}{2}.txt'.format(question, dataSetNames[dataSet], partName)
    elif dataSet == 1:
        if not isPractice: partName = '-attempt{}'.format(attemptCount)
        dataFileName = '{0}-{1}{2}.in'.format(question, dataSetNames[dataSet], partName)
    else:
        if not isPractice: partName = ''
        dataFileName = '{0}-{1}{2}.in'.format(question, dataSetNames[dataSet], partName)

    ProcessDataFile(dataFileName)

if __name__ == '__main__': main()