import bisect

def isTidy(tempnum):
    prevDigit=1

    for digit in list(str(tempnum)):
        if int(digit) < prevDigit:
            return False
        prevDigit = int(digit)
    return True


def appendIfNotZero(list, value):
    if value > 0:
        bisect.insort(list, value)
        # list.append(value)


def solveForT(n, k):
    spaces = [n]
    peopleCounter = k
    while peopleCounter > 0:
        peopleCounter -= 1
        spaceToBeOccupied = spaces.pop(-1)
        lastPersonBiggestSpace = spaceToBeOccupied
        appendIfNotZero(spaces, spaceToBeOccupied//2)
        appendIfNotZero(spaces, (spaceToBeOccupied//2) - ((spaceToBeOccupied+1) % 2))

    farest = lastPersonBiggestSpace//2
    closest = max((lastPersonBiggestSpace//2) - (((lastPersonBiggestSpace)+1)%2), -999)
    return (farest, closest)

def takeInputAndSolveEach():
    outputFile = open('q3_out.py', 'w')
    f = open('q3_in.py', 'r')
    nOfCases = int(f.readline())
    caseCounter = 0
    while caseCounter < nOfCases:
        caseCounter += 1
        inp = f.readline().split()
        n = int(inp[0])
        k = int(inp[1])
        caseSolution = solveForT(n,k)
        printCaseSolution(caseSolution, caseCounter, outputFile)


def printCaseSolution(solution, caseNumber, outputFile):
    solutionForCase = "Case #" + str(caseNumber) + ": " + str(solution[0]) + " " + str(solution[1])
    outputFile.write(solutionForCase + "\n")

if __name__ == "__main__":
    takeInputAndSolveEach()
