#!/usr/bin/python
# 2010 Round1A
''' Usage %s
'''
import logging

CurrentDebugLevel=logging.DEBUG

def ProcessCase(inFile, caseNum):
    logging.debug('Case %d', caseNum)
    param = inFile.readline().strip().split()
    lineCount = int(param[0])
    winNum = int(param[1])
    
    maxLen = 0
    lineList = []
    for i in range(0, lineCount):
        line = inFile.readline().strip()
        newLine = ''
        for c in line:
            if c == '.': continue
            newLine += c
        if maxLen < len(newLine): maxLen = len(newLine)
        if len(newLine) > 0: lineList.append(newLine)
        
    resultLines = []
    for line in lineList:
        newLine = ('.' *(maxLen - len(line))) + line
        resultLines.append(newLine)
#        logging.debug(newLine)
        
    winners = set()
    # 4 -> Horizontal, Vertical, Left to right Diagonal, Right to Left Diagonal
    countRed = [[[0 for k in range(maxLen + 2)] for j in range(len(resultLines) + 2)] for i in range(4)]
    countBlue = [[[0 for k in range(maxLen + 2)] for j in range(len(resultLines) + 2)] for i in range(4)]

    countDict = {}
    countDict['R'] = countRed
    countDict['B'] = countBlue

    for row, line in enumerate(resultLines):
        for col, c in enumerate(line):
            if c == '.': continue
            #if c in winners: continue # skip counting winners
            curCount = countDict[c]
            curCount[0][row + 1][col + 1] = curCount[0][row + 1][col] + 1
            curCount[1][row + 1][col + 1] = curCount[1][row][col + 1] + 1
            curCount[2][row + 1][col + 1] = curCount[2][row][col] + 1
            curCount[3][row + 1][col + 1] = curCount[3][row][col + 2] + 1
            for count in curCount: 
                if count[row + 1][col + 1] >= winNum: winners.add(c)
#    for d in countRed:
#        for row in d:    
#            logging.debug(row)
#        logging.debug('')
#    for d in countBlue:
#        for row in d:    
#            logging.debug(row)
#        logging.debug('')
    
    if len(winners) == 0: result = ['Neither']
    elif len(winners) == 2: result = ['Both']
    elif 'R' in winners: result = ['Red']
    elif 'B' in winners: result = ['Blue']
    else: raise Error
    
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
    
    dataSetNames = ['test', 'small', 'large']
    if dataSet == 0:
        dataFileName = '{0}-{1}.txt'.format(question, dataSetNames[dataSet])
    elif dataSet == 1:
        dataFileName = '{0}-{1}-attempt{2}.in'.format(question, dataSetNames[dataSet], attemptCount)
    else:
        dataFileName = '{0}-{1}.in'.format(question, dataSetNames[dataSet])

    ProcessDataFile(dataFileName)

if __name__ == '__main__': main()