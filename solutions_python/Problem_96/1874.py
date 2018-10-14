def readFromFile(filename):
    inputFile = open(filename, 'r')
    lineArray = []
    for line in inputFile:
        line = line.strip()
        line = line.split()
        lineArray.append(line)
    inputFile.close()
    return(lineArray)

def writeToFile(filename,listOfLines):
    inputFile = open(filename, 'w')
    for e in listOfLines:
        inputFile.write(e + '\n')
    inputFile.close()

inputList = readFromFile('B-small-attempt3.in')
outputList = []

for i in range(1,len(inputList)):
    dancerNumber = int(inputList[i][0])
    surprising = int(inputList[i][1])
    score = int(inputList[i][2])
    amount = 0
    if (score == 0):
        amount = dancerNumber
    else:
        for e in range(0,dancerNumber):
            if (int(score) >= int(inputList[i][e+3])):
                continue
            elif ((score+(score-1)+(score-1)) <= int(inputList[i][e+3])):
                amount += 1
            elif (surprising>0) and ((score+(score-2)+(score-2)) <= int(inputList[i][e+3])):
                amount += 1
                surprising -= 1
    outputList.append("Case #" + str(i) + ": " + str(amount))

writeToFile('output.txt',outputList)

