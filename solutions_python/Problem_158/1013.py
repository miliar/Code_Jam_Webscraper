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


infoList = readTestset('D-small-attempt2.in')
print(infoList)

def solveOneLine(lineList):
    x = int(lineList[0])
    r = int(lineList[1])
    c = int(lineList[2])

    maxRC = max(r,c)
    minRC = min(r,c)

    if (x > maxRC) or ((r*c)%x != 0) or (x >= (2*minRC + 1)) or (x >= 7) or (x > 3 and minRC == 2):
        return "RICHARD"
    else:
        return "GABRIEL"
    
f = open('result','w')
for i in range(len(infoList)):
    f.write("Case #")
    f.write(str(i+1))
    f.write(": ")
    f.write(str(solveOneLine(infoList[i])))
    f.write('\n')

print("closing")
f.close()
