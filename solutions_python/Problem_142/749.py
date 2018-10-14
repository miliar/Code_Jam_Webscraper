import sys, os
from collections import defaultdict

puzzles = list()

FILENAME = 'A-small-attempt1.in'

sys.setrecursionlimit(100000)


# def getDic(puzzle):
#     allLetters = set()
#     dics = list()
#     previousSet = set()
#     for p in puzzle:
#         theDic = defaultdict(int)
#         theSet = set()
#         for letter in p:
#             theDic[letter] += 1
#             theSet.add(letter)
#             allLetters.add(letter)
#         dics.append(theDic)
#         if previousSet and not previousSet == theSet:
#             return False, False
#         previousSet = theSet
#     return allLetters, dics
#
# def solve(puzzle):
#     allLetters, letterDics = getDic(puzzle)
#
#     print allLetters
#     print letterDics
#
#     if letterDics == False:
#         return 'Fegla Won'
#
#     nbActions = 0
#     for l in allLetters:
#         nbLetters = 0
#         nbPresents = 0
#         for ld in letterDics:
#             nbPresents += 1
#             nbLetters += ld[l]
#         goal = round(nbLetters / nbPresents)
#         for ld in letterDics:
#             nbActions += abs(ld[l] - goal)
#     return int(nbActions)


def getCanonicals(puzzle):
    canonicals = list()
    numbers = list()
    for p in puzzle:
        s = ''
        previousLetter = ''
        theNumbers = list()
        for l in p:
            if l != previousLetter:
                s = s + l
                previousLetter = l
                theNumbers.append(1)
            else:
                theNumbers[-1] += 1
        canonicals.append(s)
        numbers.append(theNumbers)
    return canonicals, numbers

def solve(puzzle):
    canonicals, numbers = getCanonicals(puzzle)
    #print canonicals, numbers

    if len(canonicals) == 2 and canonicals[0] != canonicals[1]:
        return 'Fegla Won'
    for i in range(len(canonicals), 1):
        if canonicals[i] != canonicals[i-1]:
            return 'Fegla Won'

    nbActions = 0
    for i, l in enumerate(canonicals[0]):
        #print i, l
        nbLetters = 0
        for n in numbers:
            nbLetters += n[i]
        goal = round(nbLetters / len(canonicals))
        for n in numbers:
            nbActions += abs(goal - n[i])
    return int(nbActions)




with open(FILENAME, 'r') as f:
    nbTestCases = int(f.readline())

    for _ in range(nbTestCases):
        puzzle = list()
        for __ in range(int(f.readline())):
            puzzle.append(f.readline().strip())
        puzzles.append(puzzle)

printResult = ''
for (i, puzzle) in enumerate(puzzles):
    #print puzzle
    #print 'Case #%s: %s\n' % (i+1, solve(puzzle))
    printResult += 'Case #%s: %s\n' % (i+1, solve(puzzle))

print printResult
#sys.exit(0)

if os.path.isfile('result'):
    os.remove('result')
with open('result', 'w') as f:
    f.write(printResult[:-1])