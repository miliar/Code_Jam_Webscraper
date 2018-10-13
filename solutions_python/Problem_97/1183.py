#!/usr/bin/python
# 2012 Qualification
''' Usage %s
'''
import logging

CurrentDebugLevel=logging.DEBUG

CacheNumbers = {}

def GetBase(n):
    bases = [1000000, 100000, 10000, 1000, 100, 10, 0]
    for d, b in enumerate(bases): 
        if n >= b: return b, 6 - d 

def GetRecycledNumbers(number):
    result = []
    base, digit = GetBase(number)
    
    original = number
    last = number
    while digit > 0:
        prefix = number // 10
        remain = number % 10
        number = remain * base + prefix
        digit -= 1
        
        if number == last: break # the number won't change
        if number <= original: continue
        result.append(number)
        last = number 
        
    return result
        

def ProcessCase(inFile, caseNum):
    logging.debug('Case %d', caseNum)
    param = inFile.readline().strip().split()
    logging.debug(param)
    A = int(param[0])
    B = int(param[1])
    
    count = 0
    for i in range(A, B + 1):
        if i not in CacheNumbers:
            CacheNumbers[i] = GetRecycledNumbers(i)
        
#        s = ''
        for n in CacheNumbers[i]:
            if n <= B: 
                count += 1
#                s += str(n) + ', '
#        if s != '': logging.debug('{}=>{}'.format(i, s))
                
    result = [count]
    
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

def DumpTable():
    #logging.debug(CheckedNumList)
    with open("cache.pickle", "wb") as outFile:
        pickle.dump(CacheNumbers, outFile)
    
def InitTable():
    try:
        cacheFile = open("cache.pickle", "rb")
        CacheNumbers = pickle.load(cacheFile)
        cacheFile.close()
    except IOError:
        # no file we generate it
        logging.debug("There's no cache. We have to do it on our own.")
        
def GenerateTable():
    for i in range(1, 1001):
        numbers = []
        CacheNumbers[i] = numbers

def main():
    logging.basicConfig(level=CurrentDebugLevel, datefmt='%Y.%m.%d %H:%M:%S', format='%(asctime)s %(levelname)-5s %(message)s')
    question = 'C'
    dataSet = 1
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

    #InitTable()
    ProcessDataFile(dataFileName)
    #DumpTable

if __name__ == '__main__': main()