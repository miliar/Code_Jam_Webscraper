#!/usr/bin/python
''' Usage %s
'''
import logging

CurrentDebugLevel=logging.DEBUG

def CountDigits(alienNum):
    countList = {}
    for i in alienNum:
        if countList.get(i) == None:
            countList[i] = -1
        #else: countList[i] += 1
    return countList

def ToDecimalByBase(resultList, base):
    result = 0
    
    digit = 1
    for i in reversed(resultList):
        result += i * digit
        digit *= base 
    
    return [result]

def Verify(resultList, result, base):
    resultStringList = []
    ordSmallA = ord('a')
    for i in resultList:
        if i > 9:
            resultStringList.append(chr(ordSmallA + i - 10))
        else: resultStringList.append(str(i))
    resultString = "".join(resultStringList)
    logging.debug(resultString)
    answer = int(resultString, base)
    if answer != result[0]:
        logging.debug("Incorrect {} != {}".format(answer, result[0]))
    
def ProcessCase(inFile, caseNum):
    logging.debug('Case %d', caseNum)
    alienNum = inFile.readline().strip()

    countList = CountDigits(alienNum)
    base = len(countList.keys())
    if base == 1: base = 2 # no base 1

    logging.info('Chunk:{}, base:{}, {}'.format(alienNum, base, countList))
    
    resultList = []
    
    countList[alienNum[0]] = 1
    resultList.append(1)

    #find second one, it's 0
    for i in alienNum[1:]:
        if countList[i] == -1:
            countList[i] = 0
            break
       
    curNum = 2
    for i in alienNum[1:]:
        if countList[i] == -1:
            countList[i] = curNum
            curNum += 1
        resultList.append(countList[i])

    logging.debug(resultList)
    
    result = ToDecimalByBase(resultList, base)
    Verify(resultList, result, base)
    
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
    #dataSet = 'small'

    dataSet = 'test'
    dataSet = 'small-attempt1'
    dataSet = 'large'

    #dataSet = 'small-practice'
    #dataSet = 'large-practice'

    ProcessDataFile('{0}-{1}.in'.format(question, dataSet))

if __name__ == '__main__': main()