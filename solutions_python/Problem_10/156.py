#!/usr/bin/python

import logging

CurrentDebugLevel=logging.DEBUG
IsWriteOutputFile=True

def ProcessCase(maxLetters, keyNum, letterNum, frequencyList):
    frequency = [int(x) for x in frequencyList]
    frequency.sort(reverse = True)
    result = 0
    weight = 0
    indexFreq = 0
    for i in xrange(maxLetters, 0, -1):
        weight += 1
        for j in xrange(keyNum):
            result += (frequency[indexFreq]* weight)
            indexFreq += 1
            if indexFreq == letterNum: break
        if indexFreq == letterNum: break
    return result
                   
def OutputResult(caseNum, outFile, result):
    logging.debug('Case #%d: %d\n' % (caseNum, result))
    if not IsWriteOutputFile: return 
    outFile.write('Case #%d: %d\n' % (caseNum, result))

def ProcessDataFile(fileName):
    inFile = open(fileName, 'r')
    line = inFile.readline()
    lineCount = int(line)
    
    outFile = None
    if IsWriteOutputFile: outFile = open(fileName + '.out.txt', 'w')
    for i in xrange(1, lineCount + 1):
        line = inFile.readline()
        params = line.strip().split()
        line = inFile.readline()
        frequencyList = line.strip().split()
        logging.debug('Case %d', i)
        result = ProcessCase(int(params[0]), int(params[1]), int(params[2]), frequencyList)
        OutputResult(i, outFile, result)
        
    if IsWriteOutputFile: outFile.close()

def main():
    logging.basicConfig(level=CurrentDebugLevel, datefmt='%Y.%m.%d %H:%M:%S', format='%(asctime)s %(levelname)-5s %(message)s')
    
    #ProcessDataFile('A-small.txt')
    #ProcessDataFile('A-small-attempt0.in')
    ProcessDataFile('A-large.in')

if __name__ == '__main__': main()