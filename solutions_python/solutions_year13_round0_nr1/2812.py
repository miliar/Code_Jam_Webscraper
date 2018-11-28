#!/usr/bin/python

import sys
import numpy as np # Used numpy for 2D array


def checkDots(twoDArray):
    countDot = 0

    for r in twoDArray:
        for c in r:
            if c == '.':
                countDot += 1

    return countDot == 0


def checkRows(twoDArray):
    for r in twoDArray:
        start = r[0]
        last = r[len(r) - 1]

        if start != '.':
            for i in range(1, len(r)):
                if i < len(r) - 1:
                    if r[i] != start:
                        break
                else:
                    if last == start or last == 'T':
                        return (start, True)

    return (start, False)


def checkCols(twoDArray):
    for c in twoDArray.transpose():
        start = c[0]
        last = c[len(c) - 1]

        if start != '.':
            for i in range(1, len(c)):
                if i < len(c) - 1:
                    if c[i] != start:
                        break
                else:
                    if last == start or last == 'T':
                        return (start, True)

    return (start, False)


def checkDiag(twoDArray):
    diag = twoDArray.diagonal()

    start = diag[0]
    last = diag[len(diag) - 1]

    if start != '.':
        for i in range(1, len(diag)):
                if i < len(diag) - 1:
                    if diag[i] != start:
                        break
                else:
                    if last == start or last == 'T':
                        return (start, True)

    return (start, False)


def checkReverDiag(twoDArray):
    reverDiag = twoDArray[::-1].diagonal()[::-1]

    start = reverDiag[0]
    last = reverDiag[len(reverDiag) - 1]

    if start != '.':
        for i in range(1, len(reverDiag)):
            if i < len(reverDiag) - 1:
                if reverDiag[i] != start:
                    break
            else:
                if last == start or last == 'T':
                    return (start, True)

    return (start, False)


def process1(inputList, caseNum, outputFile):
    arr = np.array(inputList, dtype=np.string_).reshape(4, 4)

    if not checkRows(arr)[1] and not checkCols(arr)[1]:
        if not checkDiag(arr)[1] and not checkReverDiag(arr)[1]:
            if checkDots(arr) is True:
                outputFile.write('Case #%d: Draw\n' % caseNum)
            else:
                outputFile.write('Case #%d: Game has not completed\n' % caseNum)
            return None

    if checkRows(arr)[1] is True:
        outputFile.write('Case #%d: %s won\n' % (caseNum, checkRows(arr)[0]))
        return None

    if checkCols(arr)[1] is True:
        outputFile.write('Case #%d: %s won\n' % (caseNum, checkCols(arr)[0]))
        return None

    if checkDiag(arr)[1] is True and checkDiag(arr) is not None:
        outputFile.write('Case #%d: %s won\n' % (caseNum, checkDiag(arr)[0]))
        return None

    if checkReverDiag(arr)[1] is True and checkReverDiag(arr) is not None:
        outputFile.write('Case #%d: %s won\n' % (caseNum, checkReverDiag(arr)[0]))
        return None


def lineCount(file):
    count = 0

    with open(file) as fin:
        for l in fin:
            count += 1

    return count - 1


def process(inputFile, outputFile):
    totalCases, case, rowNum = 0, 1, 1
    a = []

    size = lineCount(inputFile)

    with open(outputFile, 'w') as fout:
        with open(inputFile, 'r') as fin:
            for index, line in enumerate(fin):
                if index == 0:
                    totalCases = int(line.rstrip())
                    continue
                else:
                    l = line.rstrip()

                if not l:
                    rowNum = 1
                    process1(a, case, fout)
                    case += 1
                    del a[:]
                    continue

                token = list(l)

                if rowNum <= 4:
                    a += token
                    rowNum += 1

                if index == size:
                    process1(a, case, fout)
                    del a[:]


def main():
    if len(sys.argv) < 3:
        sys.exit('Usage: %s input_file output_file' % sys.argv[0])

    inFile = sys.argv[1]
    outFile = sys.argv[2]

    process(inFile, outFile)


if __name__ == '__main__':
    main()
