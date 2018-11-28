import sys

def checkRight(i, matrix):
    output = ""
    findCharacter = ""
    findCharacter = matrix[i]

    if findCharacter != 'T':
        firstCandidate = findCharacter if matrix[i + 1] == 'T' else matrix[i + 1]
        secondCandidate = findCharacter if matrix[i + 2] == 'T' else matrix[i + 2]
        thirdCandidate = findCharacter if matrix[i + 3] == 'T' else matrix[i + 3]

        if findCharacter == firstCandidate and findCharacter == secondCandidate and findCharacter == thirdCandidate:
            output = findCharacter + " won"
    else:
        firstCandidate = matrix[i + 1]
        secondCandidate = matrix[i + 2]
        thirdCandidate = matrix[i + 3]
        if firstCandidate == secondCandidate == thirdCandidate:
            output = firstCandidate + " won"

    return output

def checkDown(i, matrix):
    output = ""
    findCharacter = ""
    findCharacter = matrix[i]

    if findCharacter != 'T':
        firstCandidate = findCharacter if matrix[i+4] == 'T' else matrix[i+4]
        secondCandidate = findCharacter if matrix[i+4+4] == 'T' else matrix[i+4+4]
        thirdCandidate = findCharacter if matrix[i+4+4+4] == 'T' else matrix[i+4+4+4]

        if findCharacter == firstCandidate and findCharacter == secondCandidate and findCharacter == thirdCandidate:
            output = findCharacter + " won"
    else:
        firstCandidate = matrix[i+4]
        secondCandidate = matrix[i+4+4]
        thirdCandidate = matrix[i+4+4+4]
        if firstCandidate == secondCandidate == thirdCandidate:
            output = firstCandidate + " won"

    return output

def checkTopLeftToBottonRight(i, matrix):
    output = ""
    findCharacter = ""
    findCharacter = matrix[i]

    if findCharacter != 'T':
        firstCandidate = findCharacter if matrix[5] == 'T' else matrix[5]
        secondCandidate = findCharacter if matrix[10] == 'T' else matrix[10]
        thirdCandidate = findCharacter if matrix[15] == 'T' else matrix[15]

        if findCharacter == firstCandidate and findCharacter == secondCandidate and findCharacter == thirdCandidate:
            output = findCharacter + " won"
    else:
        firstCandidate = matrix[5]
        secondCandidate = matrix[10]
        thirdCandidate = matrix[15]
        if firstCandidate == secondCandidate == thirdCandidate:
            output = firstCandidate + " won"

    return output

def checkTopRightToBottonLeft(i, matrix):
    output = ""
    findCharacter = ""
    findCharacter = matrix[i]

    if findCharacter != 'T':
        firstCandidate = findCharacter if matrix[6] == 'T' else matrix[6]
        secondCandidate = findCharacter if matrix[9] == 'T' else matrix[9]
        thirdCandidate = findCharacter if matrix[12] == 'T' else matrix[12]

        if findCharacter == firstCandidate and findCharacter == secondCandidate and findCharacter == thirdCandidate:
            output = findCharacter + " won"
    else:
        firstCandidate = matrix[6]
        secondCandidate = matrix[9]
        thirdCandidate = matrix[12]
        if firstCandidate == secondCandidate == thirdCandidate:
            output = firstCandidate + " won"

    return output

f = open("test.in")

numberOfTestCase = f.readline()

for testCase in xrange(int(numberOfTestCase)):
    draw = True;
    matrix = list(f.read(20))
    matrix.remove("\n")
    matrix.remove("\n")
    matrix.remove("\n")
    matrix.remove("\n")
    f.read(1)

   #print matrix

    for i in xrange(len(matrix)):
        winner = ""

        # right
        if i == 0 or i == 4 or i == 8 or i == 12:
            if matrix[i] != '.':
                winner = checkRight(i, matrix)
                if (winner != ""):
                    print "Case #" + str(testCase+1) + ": " + winner
                    draw = False
                    break

        # down
        if i == 0 or i == 1 or i == 2 or i == 3:
            if matrix[i] != '.':
                winner = checkDown(i, matrix)
                if (winner != ""):
                    print "Case #" + str(testCase+1) + ": " + winner
                    draw = False
                    break

        # top left to bottom right
        if i == 0:
            if matrix[i] != '.':
                winner = checkTopLeftToBottonRight(i, matrix)
                if (winner != ""):
                    print "Case #" + str(testCase+1) + ": " + winner
                    draw = False
                    break

        # top right to bottom left
        if i == 3:
            if matrix[i] != '.':
                winner = checkTopRightToBottonLeft(i, matrix)
                if (winner != ""):
                    print "Case #" + str(testCase+1) + ": " + winner
                    draw = False
                    break

    if i == 15 and matrix.count('.') == 0:
        sys.stdout.write("Case #")
        sys.stdout.write(str(testCase+1))
        sys.stdout.write(": Draw")
        print
    elif draw:
        sys.stdout.write("Case #")
        sys.stdout.write(str(testCase+1))
        sys.stdout.write(": Game has not completed")
        print

