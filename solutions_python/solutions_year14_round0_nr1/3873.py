import sys

def main():
    filePath = getFilePath()
    if filePath:
        foutput = open('solution', 'w')
        with open(filePath) as f:
            testCasesCount = int(f.readline())
            for testCaseIndex in range(testCasesCount):
                testCase = readTestCase(f)
                solution = solveTestCase(testCase)
                foutput.write('Case #' + str(testCaseIndex + 1) + ': ' + solution + '\n')
        foutput.close()

def getFilePath():
    return sys.argv[1] if len(sys.argv) > 1 else None

def readTestCase(f):
    firstGuess = int(f.readline())
    firstRows = []
    for rowIndex in range(4):
        firstRows.append(f.readline().strip().split(' '))
    secondGuess = int(f.readline())
    secondRows = []
    for rowIndex in range(4):
        secondRows.append(f.readline().strip().split(' '))
    return [
        {
            'guess': firstGuess - 1,
            'cards': firstRows
        },
        {
            'guess': secondGuess - 1,
            'cards': secondRows
        }
    ]

def solveTestCase(testCase):
    firstGuess = testCase[0]['guess']
    firstRow = testCase[0]['cards'][firstGuess]
    secondGuess = testCase[1]['guess']
    secondRow = testCase[1]['cards'][secondGuess]

    coincidences = 0
    lastCoincidentCard = None
    for i in firstRow:
        if i in secondRow:
            coincidences += 1
            lastCoincidentCard = i

    if coincidences == 0:
        solution = 'Volunteer cheated!'
    elif coincidences == 1:
        solution = str(lastCoincidentCard)
    else:
        solution = 'Bad magician!'
    return solution

if __name__ == '__main__':
    main()