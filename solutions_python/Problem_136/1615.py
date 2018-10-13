import sys

sys.path.insert(0, 'H:\dev\workspaces\competition\Google code Jam\utilities')
import codeJamHelper

inputFileName = 'B-large.in'
outputFileName = 'B-large.out'


def computeTimeCost(gainPerSecond, goalToReach):
    return float(goalToReach) / float(gainPerSecond)


lines = codeJamHelper.readFile(inputFileName)
size = int(lines[0])
iterator = 1
result = []
for index in range(size):
    entry = codeJamHelper.splitString(lines[iterator])
    C = float(entry[0])
    F = float(entry[1])
    X = float(entry[2])
    bestChoiceReached = False
    gainPerSecond = 2
    timeSpent = 0
    while not bestChoiceReached:
        xCost = computeTimeCost(gainPerSecond, X)
        fCost = computeTimeCost(gainPerSecond, C)
        xCostWithFarm = computeTimeCost(gainPerSecond + F, X)
        bestChoiceReached = xCost < (fCost + xCostWithFarm)
        timeSpent += (fCost, xCost)[bestChoiceReached]
        gainPerSecond += F

    stringValue = codeJamHelper.convertFloatToString(timeSpent)
    codeJamHelper.appendResult(stringValue, result)
    iterator += 1

print result
codeJamHelper.storeLines(result, outputFileName)