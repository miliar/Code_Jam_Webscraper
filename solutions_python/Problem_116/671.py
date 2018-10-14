def testLine(fourCharacters):
    if all([character == "X" or character == "T" for character in fourCharacters]):
        return "X"
    if all([character == "O" or character == "T" for character in fourCharacters]):
        return "O"
    else:
        return False

inputFile = open("A-small-attempt1.in", "r")
#inputFile = open("QualificationAsmall.in", "r")

outputFile = open("QualificationAsmall.txt", "w")

cases = int(inputFile.readline().strip())
boards = inputFile.read().split("\n\n")
for caseIndex in range(1, cases + 1):
    finalResult = ""
    currentBoard = boards[caseIndex - 1].split("\n")
    for lineIndex in range(4):
        result = testLine(currentBoard[lineIndex])
        if result:
            finalResult = "%s won" % result

        result = testLine([currentBoard[line][lineIndex] for line in range(4)])
        if result:
            finalResult = "%s won" % result

    result = testLine([currentBoard[index][index] for index in range(4)])
    if result:
        finalResult = "%s won" % result
    result = testLine([currentBoard[index][3 - index] for index in range(4)])
    if result:
        finalResult = "%s won" % result

    if not finalResult:
        if all(["." not in line for line in currentBoard]):
            finalResult = "Draw"
        else:
            finalResult = "Game has not completed"
    outputFile.write("Case #%d: %s\n" % (caseIndex, finalResult))

inputFile.close()
outputFile.close()

