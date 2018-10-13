import math
def readInput():
    inputList = list()
    f = open('A-small-attempt0.in')
    caseNum = int(f.readline().strip('\n'))
    for i in range(0, caseNum):
        line = f.readline().strip('\n')
        inputList.append([int(num) for num in line.split(" ")])
    f.close()
    return inputList

def processData(inputList):
    resultList = list()
    for pair in inputList:
        r = pair[0]
        t = pair[1]
        result = (-2 * r + 1 + math.sqrt((2 * r - 1) * (2 * r - 1) + 8 * t))/ 4
        result = int(math.floor(result))
        resultList.append(result)
    return resultList

def outputResult(resultList):
    caseCounter = 1
    f = open('result.out', 'w')
    for result in resultList:
        line = "Case #%d: %d\n" % (caseCounter, result)
        caseCounter += 1
        f.write(line)
    f.close()

def main():
    inputList = readInput()
    resultList = processData(inputList)
    outputResult(resultList)
main()
