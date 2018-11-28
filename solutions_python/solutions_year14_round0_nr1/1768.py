__author__ = 'Drazen'

BAD_MAGICIAN = 'Bad magician!'
VOLUNTEER_CHEATED = 'Volunteer cheated!'

def FindCard(testCase):
    firstLine = testCase[int(testCase[0][0])]
    secondLine = testCase[int(testCase[5][0]) + 5]
    commonElements = set(firstLine) & set(secondLine)
    if len(commonElements) == 0:
        return VOLUNTEER_CHEATED
    if len(commonElements) == 1:
        return commonElements.pop()
    if len(commonElements) > 1:
        return BAD_MAGICIAN


if __name__ == "__main__":
    inputFile = open('H:/development/GoogleCodeJam/2014/A/A-small-attempt0.in', mode='r')
    outputFile = open('H:/development/GoogleCodeJam/2014/A/output.txt', mode='w')
    resultLine = 'Case #{0}: {1}'
    inputFile.seek(0)
    numberOfTests = int(inputFile.readline())
    for i in range(numberOfTests):
        testCase = []
        for j in range(10):
            testCase.append(inputFile.readline().split())
        outputFile.write( str.format(resultLine, i+1, FindCard(testCase) + '\n'))
    inputFile.close()
    outputFile.close()