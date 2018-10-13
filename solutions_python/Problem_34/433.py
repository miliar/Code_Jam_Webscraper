#!/usr/bin/python
''' Usage %s
'''
import logging
import re

CurrentDebugLevel=logging.DEBUG

wordBank = []
dictionary = []

def ProcessCase(inFile, caseNum):
    logging.debug('Case %d', caseNum)
    wordContent = inFile.readline().strip()
    wordContent = wordContent.replace("(", "[")
    wordContent = wordContent.replace(")", "]")
    
    logging.debug(wordContent)
    
    regex = re.compile(wordContent)
    count = 0
    
    for i in range(0, len(wordBank)):
        if regex.match(wordBank[i]) != None: count += 1
    
    result = [count]
    
    return result

def ProcessCase2(inFile, caseNum):
    regex = re.compile("[abcdefghijklmno][abcdijklmno][abcdijklmno][abcdijklmno][abcdijklmno][abcdijklmno][abcd][abcd][abcd][abcd][abcdijklmno][abcd][abcd][abcd][abcd]")
    #regex = re.compile("[abcd][abcd][abcd][abcd][abcd][abcd][abcd][abcd][abcd][abcd][abcd][abcd][abcd][abcd][abcd]")
    count = 0
    for i in range(0, 5000):
        if regex.match("adjbcmcbcabcabc") != None: count += 1
    result = [count]
    
    return result 

def OutputResult(outFile, caseNum, result):
    value = result[0]
    outFile.write("Case #{0}: {1}\n".format(caseNum, value))
    logging.debug("Case #{0}: {1}\n".format(caseNum, value))

def ProcessDataFile(fileName):
    inFile = open(fileName, 'r')
    param = inFile.readline().split()
    wordLen = int(param[0])
    wordNum = int(param[1])
    caseNum = int(param[2])
    lineCount = wordNum
    
    for i in range(0, wordNum):
        wordBank.append(inFile.readline().strip())

    logging.debug(wordBank)
    
    lineCount = caseNum
    outFile = open(fileName + '.out.txt', 'w')
    for i in range(1, lineCount + 1):
        result = ProcessCase(inFile, i)
        OutputResult(outFile, i, result)
    outFile.close()

def main():
    logging.basicConfig(level=CurrentDebugLevel, datefmt='%Y.%m.%d %H:%M:%S', format='%(asctime)s %(levelname)-5s %(message)s')
    question = 'A'
    #dataSet = 'small-attempt0'
    dataSet = 'large'
    #dataSet = 'test'
    #dataSet = 'small-practice'
    #dataSet = 'large-practice'

    ProcessDataFile('{0}-{1}.in'.format(question, dataSet))

if __name__ == '__main__': main()