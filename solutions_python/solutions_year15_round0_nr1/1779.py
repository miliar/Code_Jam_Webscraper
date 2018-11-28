def readTestset(testset):
    fo = open(testset,'r+')
    line = fo.readline()
    testCases = int(line)
    print("test cases:\t", testCases)
    infoList = []
    for i in range(testCases):
        line = fo.readline()
        infoList.append(line.split())
    return infoList


infoList = readTestset('A-large.in')
print(infoList)

def solveOneLine(lineList):
    n = int(lineList[0])
    dgts = lineList[1]
    tillNow = 0
    mine = 0
    for i in range(n+1):
        if i > tillNow:
            mine += i - tillNow
            tillNow = i
        tillNow += int(dgts[i])
    return mine

f = open('result','w')
for i in range(len(infoList)):
    f.write("case #")
    f.write(str(i+1))
    f.write(": ")
    f.write(str(solveOneLine(infoList[i])))
    f.write('\n')

print("closing")
f.close()
