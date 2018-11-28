import sys

caseMatrixList = list()
caseBooleanMatrixList = list()

def getSplitedList(s):
    s = s.strip('\n')
    sList = s.split(" ")
    return [int(i) for i in sList] 

def readFile():
    fileName = sys.argv[1]
    f = open(fileName)
    caseNum = int(f.readline().strip('\n'))
    for caseIndex in range(caseNum):
        caseMatrix = list()
        caseBooleanMatrix = list()
        dimensionList = getSplitedList(f.readline())
        lineNum = dimensionList[0]
        colNum = dimensionList[1]
        for lineIndex in range(lineNum):
            caseMatrix.append(getSplitedList(f.readline()))
            caseBooleanMatrix.append([False] * colNum)
        caseMatrixList.append(caseMatrix)
        caseBooleanMatrixList.append(caseBooleanMatrix)

def process(caseMatrix, caseBooleanMatrix):
    lineIndex = 0
    # line order
    for line in caseMatrix:
        lineMax = max(line)
        for colIndex in range(len(line)):
            if line[colIndex] == lineMax:
                caseBooleanMatrix[lineIndex][colIndex] = True
        lineIndex += 1
    # col order
    lineNum = len(caseMatrix)
    colNum = len(caseMatrix[0])
    for colIndex in range(colNum):
        colList = [line[colIndex] for line in caseMatrix]
        colMax = max(colList)
        for lineIndex in range(lineNum):
            if caseMatrix[lineIndex][colIndex] == colMax:
                caseBooleanMatrix[lineIndex][colIndex] = True

def result():
    caseCounter = 1
    f = open('result.out', 'w')
    for boolMatrix in caseBooleanMatrixList:
        possible = True
        for line in boolMatrix:
            for boolean in line:
                if boolean == False:
                    possible = False
                    break
        resultStr = ""
        if possible:
            resultStr = "Case #%d: YES\n" % caseCounter
        else:
            resultStr = "Case #%d: NO\n" % caseCounter
        f.write(resultStr)        
        caseCounter += 1 
    f.close()        

def main():
    readFile()
    caseNum = len(caseMatrixList)
    for caseIndex in range(caseNum):
        process(caseMatrixList[caseIndex], caseBooleanMatrixList[caseIndex])
    result()
main()
    
