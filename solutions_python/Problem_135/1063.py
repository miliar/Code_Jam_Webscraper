__author__ = 'viv'


def getRow(file, firstAnswer):
    for i in range(1, 5):
        if i == firstAnswer:
            firstRow = (set(int(elem) for elem in file.readline().split()))
        else:
            file.readline()
    return firstRow


def resolveMagickTrick(file):
    firstAnswer = int(inFile.readline())
    firstRow = getRow(file, firstAnswer)
    secondAnswer = int(inFile.readline())
    secondRow = getRow(inFile, secondAnswer)
    rowIntersection = set.intersection(firstRow, secondRow)
    lenAnswer = len(rowIntersection)
    if lenAnswer == 1:
        return str(rowIntersection.pop())
    elif lenAnswer > 1:
        return 'Bad magician!'
    return 'Volunteer cheated!'

if __name__ == '__main__':
    inFile = open('A-small-attempt1.in','r')
    numberOfTests = int(inFile.readline())
    outFile = open('A-small-attempt1.out','w')
    for i in range(1, numberOfTests + 1):
        answer = resolveMagickTrick(inFile)
        outFile.write('Case #%d: %s\n' % (i, answer))