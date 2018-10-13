#!/usr/bin/python
# 2012 Qualification
''' Usage %s
'''
import logging

CurrentDebugLevel=logging.DEBUG

def ProcessCase(inFile, caseNum, mappingTable):
    logging.debug('Case %d', caseNum)
    param = inFile.readline().strip()
    logging.debug(param)
    
    res = ''
    
    for i in param:
        c = ' '
        if i != ' ': c = mappingTable[i]
        res += c
    
    result = [res]
    
    return result

def OutputResult(outFile, caseNum, result):
    value = result[0]
    outFile.write("Case #{}: {}\n".format(caseNum, value))
    logging.debug("Case #{}: {}\n".format(caseNum, value))

def InitMappingTable():
    input = ["z", "y qee", "ejp mysljylc kd kxveddknmc re jsicpdrysi", "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "de kr kd eoya kw aej tysr re ujdr lkgc jv"]
    answer =["q", "a zoo", "our language is impossible to understand", "there are twenty six factorial possibilities", "so it is okay if you want to just give up"]
    
    mappingTable = {}
    
    for g, s in zip(input, answer):
        for i, j in zip(g, s):
            if i == ' ': continue
            if i in mappingTable and j != mappingTable[i]:
                logging.debug("Conflict: {} => {}, => {}".format(i, mappingTable[i], j))
                continue
            mappingTable[i] = j
            
    return mappingTable

def ProcessDataFile(fileName):
    
    mappingTable = InitMappingTable()
    #logging.debug('mapping ={}'.format(len(mappingTable)))
    #logging.debug(mappingTable)
    
    backMapping = []
    for k in sorted(mappingTable.keys()):
        logging.debug("{}=>{}".format(k, mappingTable[k]))
#        backMapping.append(mappingTable[k])
#    for i in sorted(backMapping):
#        logging.debug(i)
    
    inFile = open(fileName, 'r')
    line = inFile.readline()
    lineCount = int(line)
    outFile = open(fileName + '.out.txt', 'w')
    for i in range(1, lineCount + 1):
        result = ProcessCase(inFile, i, mappingTable)
        OutputResult(outFile, i, result)
    outFile.close()

def main():
    logging.basicConfig(level=CurrentDebugLevel, datefmt='%Y.%m.%d %H:%M:%S', format='%(asctime)s %(levelname)-5s %(message)s')
    question = 'A'
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

    ProcessDataFile(dataFileName)

if __name__ == '__main__': main()