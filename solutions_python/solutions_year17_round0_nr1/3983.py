import fileinput
import sys
from itertools import combinations

counter = 0

def isLineupSolved( lineup ):
    return "-" not in lineup

def possibleFlipIndexes( lineup, flipperLength ):
    length = len(lineup)
    possibleIndexes = []
    for i in range(0, length - flipperLength + 1):
        possibleIndexes.append(i)
    return possibleIndexes

def flipAtIndex( lineup, flipperLength, index ):
    lineupList = list(lineup)
    for i in range(index, index + flipperLength):
        if lineupList[i] == '-':
            lineupList[i] = '+'
        else:
            lineupList[i] = '-'
    return "".join(lineupList)

def getCombinations(input):
    output = sum([map(list, combinations(input, i)) for i in range(len(input) + 1)], [])
    return output

for line in fileinput.input():
    if (counter != 0):
        problemArray = line.split(' ', 1 )
        problemString = problemArray[0]
        flipperLength = int(problemArray[1])

        lowestMoves = None

        if isLineupSolved(problemString):
            lowestMoves = 0

        for moveSet in getCombinations(possibleFlipIndexes(problemString, flipperLength)):
            if lowestMoves != None and len(moveSet) > lowestMoves:
                continue
            moveString = problemString[:]
            for move in moveSet:
                moveString = flipAtIndex(moveString, flipperLength, move)
                if isLineupSolved(moveString):
                    if lowestMoves == None:
                        lowestMoves = len(moveSet)
                    else:
                        if len(moveSet) < lowestMoves:
                            lowestMoves = len(moveSet)

        if lowestMoves == None:
            lowestMoves = "IMPOSSIBLE"

        print('Case #' + str(counter) + ': ' + str(lowestMoves))

    counter += 1

sys.stdout.flush()
