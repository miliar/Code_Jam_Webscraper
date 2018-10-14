

import math

def stdBest(totalScore):
    return math.ceil(totalScore/3.0)

def surpBest(totalScore):
    result = stdBest(totalScore)
    if (totalScore in (0, 1, 29, 30)) or (totalScore % 3 == 1):
        return result
    else:
        return result+1

def readCase(theFile):
    return theFile.readline().strip()

def writeCase(theFile, caseNumber, answer):
    theLine = "Case #%d: %s"%(caseNumber, answer)
    theFile.write(theLine + "\n")
    return

def solveCase(aLine):
    numbers = [int(x) for x in aLine.split()]
    numScores = numbers[0]
    availSurps = numbers[1]
    goalScore = numbers[2]
    scores = numbers[3:3+numScores]
    totalPasses = 0
    for score in scores:
        if stdBest(score) >= goalScore:
            totalPasses += 1
        elif (availSurps > 0) and (surpBest(score) >= goalScore):
            totalPasses += 1
            availSurps -= 1
    return str(totalPasses)


def main(fileName):
    f = open(fileName, "U")
    g = open(fileName+".out", "w")
    cases = int(f.readline())
    for x in xrange(cases):
        writeCase(g, x+1, solveCase(readCase(f)))
    f.close()
    g.close()
    return

if __name__ == "__main__":
    from sys import argv
    main(argv[1])
