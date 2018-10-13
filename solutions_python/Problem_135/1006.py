# Google Code Jam 2014 - Magic Trick
# Guy Weizman

import sys

__author__ = 'Guy Weizman'


# Receives two sorted arrays, finds corresponding numbers
def solveCase(row1, row2):
    corresponding = list()
    for num1 in row1:
        for num2 in row2:
            if (num1 == num2):
                corresponding.append(num1)
            if (num1 < num2):
                break;
    if (len(corresponding) == 1):
        return corresponding[0]
    if (len(corresponding) > 1):
        return "Bad magician!"
    return "Volunteer cheated!"


if (len(sys.argv) != 2):
    print 'Syntax: python cookie.py FILE_PATH [Without .in]'
    exit()

file = sys.argv[1]

INPUTLINES = 4

readFile = open(file + '.in', 'r')
writeFile = open(file + '.out', 'w')

testCases = int(readFile.readline())

for i in range(testCases):
    row = int(readFile.readline())
    for j in range(INPUTLINES):
        if j + 1 == row:
            row1 = readFile.readline().rstrip()
        else:
            readFile.readline()
    row = int(readFile.readline())
    for j in range(INPUTLINES):
        if j + 1 == row:
            row2 = readFile.readline().rstrip()
        else:
            readFile.readline()
    writeFile.write("Case #" + str(i + 1) + ": " + solveCase(sorted(row1.split()), sorted(row2.split())) + "\n")