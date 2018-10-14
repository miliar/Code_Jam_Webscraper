#!/usr/bin/python

import sys
import math


def palindrome(num):
    for i in range(len(num) // 2):
        if num[i] != num[-1 - i]:
            return False

    return True


def process1(s, e, caseNum, outputFile):
    palCount = 0L

    start = long(math.ceil(math.sqrt(s)))
    end = long(math.sqrt(e)) + 1

    for i in range(start, end):
        if palindrome(str(i**2)) and palindrome(str(i)):
            palCount += 1

    outputFile.write('Case #%d: %d\n' % (caseNum, palCount))


def process(inputFile, outputFile):
    totalCases, case = 0, 1
    start = end = 0

    with open(outputFile, 'w') as fout:
        with open(inputFile, 'r') as fin:
            for index, line in enumerate(fin):
                if index == 0:
                    totalCases = int(line.rstrip())
                    continue
                else:
                    l = line.rstrip()

                tokens = l.split()

                start = long(tokens[0])
                end = long(tokens[1])

                process1(start, end, case, fout)
                case += 1


def main():
    if len(sys.argv) < 3:
        sys.exit('Usage: %s input_file output_file' % sys.argv[0])

    inFile = sys.argv[1]
    outFile = sys.argv[2]

    process(inFile, outFile)


if __name__ == '__main__':
    main()
