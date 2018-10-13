import sys

testCases = []

def readInput(inputFile):

    global testCases

    theFile = open(inputFile, 'r')
    numberCases = int(theFile.readline())
    for i in range(numberCases):
        line = theFile.readline().split()
        testCases.append(line)

def computeTestCase(testCase):

    maxShyness = int(testCase[0])
    shynessString = testCase[1]

    total = 0
    addedmember = 0

    for i in range(len(shynessString)):

        shyness = int(shynessString[i])

        if shyness == 0 and (total-i) == 0:
            addedmember += 1
            total += 1

        total += shyness

        if total >= (maxShyness):

            return addedmember

def solve(inputFile):

    fileOut = ""

    readInput(inputFile)

    for i in range(len(testCases)):
        case = testCases[i]
        fileOut += "Case #"+str(i+1)+": "+str(computeTestCase(case))
        if i != (len(testCases)-1):
            fileOut += "\n"

    print(fileOut)

    outFile = open("Output.txt", "w")
    outFile.write(fileOut)
    outFile.close()

solve(sys.argv[1])
