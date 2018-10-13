def magicTrick(inputFile):
    input = open(inputFile)
    inputLines = input.readlines()
    input.close()
    numberOfTests = int(inputLines[0])
    lineReading = 1
    output = []
    for i in range(0,numberOfTests):
        firstGuess = int(inputLines[lineReading][0])
        firstGrid = getGrid(inputLines,lineReading)
        lineReading = lineReading + 5
        secondGuess = int(inputLines[lineReading][0])
        secondGrid = getGrid(inputLines,lineReading)
        lineReading = lineReading + 5
        answer = solveTestCase(firstGuess,secondGuess,firstGrid,secondGrid)
        output.append("Case #" + str(i+1) + ": " + answer + "\n")
    outputFile = open("outputFile.txt","w")
    outputFile.writelines(output)
    outputFile.close()

def solveTestCase(firstGuess,secondGuess,firstGrid,secondGrid):
    #The trick uses 1 based counting instead of 0
    possibleFirst = firstGrid[firstGuess-1]
    possibleSecond = secondGrid[secondGuess-1]
    candidates = list(set(possibleFirst).intersection(set(possibleSecond)))
    if len(candidates) == 0:
        return "Volunteer cheated!"
    elif len(candidates) > 1:
        return "Bad magician!"
    else:
        return str(candidates[0])

def getGrid(inputLines,lineReading):
    grid = []
    for i in [1,2,3,4]:
        line = [int(x) for x in (inputLines[lineReading+i]).split()]
        grid.append(line)
    return grid
