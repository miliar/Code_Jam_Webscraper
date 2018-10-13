fIn = open("input.in","r")
fOut = open("output.txt","w")
numberOfCasesStr = fIn.readline()
numberOfCasesSplit = numberOfCasesStr.split()
numberOfCases = int(numberOfCasesSplit[0])
for i in range(numberOfCases):
    line = fIn.readline()
    numbers = line.split()
    cost = float(numbers[0])
    extraNumber = float(numbers[1])
    goal = float(numbers[2])
    timeTaken = 0
    count = 0
    nTh = goal/(2+count * extraNumber)
    mTh = cost/(2+count * extraNumber) + goal/(2+(count + 1)*extraNumber)
    while nTh > mTh:
        timeTaken = timeTaken + cost/(2+ count * extraNumber)
        count = count + 1
        nTh = goal/(2+count * extraNumber)
        mTh = cost/(2+count * extraNumber) + goal/(2+(count + 1)*extraNumber)
    timeTaken = timeTaken + goal/(2+count * extraNumber)
    timeTakenStr = "{:.7f}".format(timeTaken)
    output = "Case #{}: ".format(i+1) + timeTakenStr
    fOut.write(output)
    fOut.write("\n")
fIn.close()
fOut.close()


