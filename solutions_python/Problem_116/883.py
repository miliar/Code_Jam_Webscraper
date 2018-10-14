inputList = list()
# 0 - O win
# 1 - X win
# 2 - draw
# 3 - not finish
resultList = list()

def getInput():
    f = open("A-large.in")
    caseNum = int(f.readline().strip('\n'))
    for i in range(caseNum):
        caseList = list()
        for j in range(4):
            caseList.append(f.readline().strip('\n'))
        blankLine = f.readline()
        inputList.append(caseList)
    f.close()
def process(caseList):
    xResult = 0
    yResult = 0
    finish = True
    # line judge
    for line in caseList:
        if line.count('.'):
            finish = False
        if line.count('X') == 4 or (line.count('X') == 3 and line.count('T') == 1):
            xResult = 1
            break
        if line.count('O') == 4 or (line.count('O') == 3 and line.count('T') == 1):
            yResult = 1
            break
    # col judge
    colList = zip(*caseList)
    for col in colList:
        if col.count('X') == 4 or (col.count('X') == 3 and col.count('T') == 1):
            xResult = 1
            break
        if col.count('O') == 4 or (col.count('O') == 3 and col.count('T') == 1):
            yResult = 1
            break
    # diagnose judge
    diagStrA = caseList[0][0] + caseList[1][1] + caseList[2][2] + caseList[3][3]
    diagStrB = caseList[0][3] + caseList[1][2] + caseList[2][1] + caseList[3][0]
    if diagStrA.count('X') == 4 or (diagStrA.count('X') == 3 and diagStrA.count('T') == 1):
        xResult = 1
    if diagStrA.count('O') == 4 or (diagStrA.count('O') == 3 and diagStrA.count('T') == 1):
        yResult = 1
    if diagStrB.count('X') == 4 or (diagStrB.count('X') == 3 and diagStrB.count('T') == 1):
        xResult = 1
    if diagStrB.count('O') == 4 or (diagStrB.count('O') == 3 and diagStrB.count('T') == 1):
        yResult = 1
    if xResult == 1 and yResult == 1:
        resultList.append(2)
    if xResult == 0 and yResult == 1:
        resultList.append(0)
    if xResult == 1 and yResult == 0:
        resultList.append(1)
    if xResult == 0 and yResult == 0:
        if finish:
            resultList.append(2)
        else:
            resultList.append(3)

def printResult():
    output = open("result.out", 'w')
    i = 0
    for result in resultList:
        i += 1
        resultStr = ""
        if result == 0:
            resultStr = "Case #%d: O won\n" % i
        if result == 1:
            resultStr = "Case #%d: X won\n" % i
        if result == 2:
            resultStr = "Case #%d: Draw\n" % i
        if result == 3:
            resultStr = "Case #%d: Game has not completed\n" % i
        output.write(resultStr)
    output.close()

def main():
    getInput()
    for case in inputList:
        process(case)
    printResult()

main()
