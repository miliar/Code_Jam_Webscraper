inputFile = open("B-small-attempt0.in", 'r')
outputFile = open("output.out", 'w')

def getSum(C, X, F, n) :
    #print("C",C,"X",X,"F",F,"n",n)
    result = 0
    for k in range(0, n) :
        result = result + C/(2.0 + F * k)
    result = result + X/(2.0 + F * n)
    return round(result, 7)

caseNum = 0
lineCount = 0
totalCase = 0
totalTime = 0
while 1:
    line = inputFile.readline()
    lineCount = lineCount + 1
    timeList = []
    if not line :
        break
    if lineCount == 1 :
        totalCase = str(line.replace('\n',''))
    else :
        caseNum = caseNum + 1
        C, F, X = line.replace('\n','').split(' ')
        C, F, X = float(C), float(F), float(X)
        timeList.append(X/2.0)
        for n in range(1, 1000000) :
            time = getSum(C, X, F, n)
            totalTime = min(timeList)
            if totalTime > time :
                timeList.append(time)
            else :
                break
        outputFile.write("Case #" + str(caseNum) + ": " + str(totalTime) + "\n")

inputFile.close()
outputFile.close()
