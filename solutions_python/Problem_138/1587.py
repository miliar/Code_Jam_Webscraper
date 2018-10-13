import sys

sys.path.insert(0, 'H:\dev\workspaces\competition\Google code Jam\utilities')
import codeJamHelper

inputFileName = 'input.test'
outputFileName = 'output.test'

inputFileName = 'D-large.in'
outputFileName = 'D-large.out'


def computeScoreWithCheat(sortedNaomiEntry, sortedKenEntry, cheatList):
    score = 0
    rangeStart = 0
    for i in range(len(sortedNaomiEntry)):
        trueValue = sortedNaomiEntry[i]
        lowestElement = sortedKenEntry[0]
        highestElement = sortedKenEntry[len(sortedKenEntry) - 1]

        if trueValue > lowestElement:
            sortedKenEntry.remove(lowestElement)
        else:
            sortedKenEntry.remove(highestElement)
            score +=1

    return score


def computeScore(sortedNaomiEntry, sortedKenEntry):
    score = 0
    rangeStart = 0
    for entry in sortedNaomiEntry:
        temp = rangeStart
        cantDoBetter = False
        for i in range(len(sortedKenEntry) - rangeStart):
            if sortedKenEntry[len(sortedKenEntry) - i - 1] > entry:
                temp = len(sortedKenEntry) - i
                cantDoBetter = True
            else:
                break
        rangeStart = temp
        if cantDoBetter:
            score += 1
        else:
            break
    return score


lines = codeJamHelper.readFile(inputFileName)
size = int(lines[0])
iterator = 1
result = []
for index in range(size):
    entrySize = codeJamHelper.splitString(lines[iterator])
    entrySize = int(entrySize[0])
    naomiEntries = codeJamHelper.splitString(lines[iterator + 1])
    kenEntries = codeJamHelper.splitString(lines[iterator + 2])

    naomiEntries = [float(entry) for entry in naomiEntries]
    kenEntries = [float(entry) for entry in kenEntries]
    naomiFakeEntries = [float(entry - 0.0000001) for entry in kenEntries]

    naomiEntries.sort()
    kenEntries.sort()
    naomiFakeEntries.sort()

    print naomiEntries
    print kenEntries
    warScore = entrySize - computeScore(naomiEntries, kenEntries)
    cheatWarScore = entrySize - computeScoreWithCheat(naomiEntries, kenEntries, naomiFakeEntries)

    print warScore, cheatWarScore

    resultContent = str(cheatWarScore) + ' ' + str(warScore)
    codeJamHelper.appendResult(resultContent, result)
    iterator += 3

print result
codeJamHelper.storeLines(result, outputFileName)