import math
from math import *

in_lines = []
in_pos = 0
out_lines = []

'''------------Read data block-----------'''


def readInput():
    global in_lines
    with open('test.in') as f:
        in_lines = f.readlines()


def saveOutput():
    global out_lines
    text_file = open("test.out", "w")
    for s in out_lines:
        text_file.write(s + '\n')
    text_file.close()


def readNextLine():
    global in_pos
    in_pos += 1
    return in_lines[in_pos - 1].replace("\n", "")


'''--------------------------------------'''

'''---------Data analysing block---------'''
pancakes = []
usePancakes = 0
square = 0

def cleanUpLines():
    global pancakes
    global usePancakes
    pancakes = []


def addLine(line):
    global lines

    splitWords = line.split()
    pancakes.append([float(splitWords[0]), float(splitWords[1])])

    pancakes.sort(key=lambda x: x[0])

def solver():
    global square

    pancakes.reverse()
    square = getSquare()
    print square

    while len(pancakes) > usePancakes:
        deleteSmallestOne()

def getSquare():
    s = pancakes[0][0] * pancakes[0][0] * math.pi + 2.0 * math.pi * pancakes[0][0] * pancakes[0][1]
    if len(pancakes) > 1:
        for i in range(len(pancakes) - 1):
            s += 2.0 * math.pi * pancakes[i + 1][0] * pancakes[i + 1][1]

    return s

def deleteSmallestOne():
    global pancakes
    global square

    smallestSquare = 9999999999999.0
    smallestId = 0

    for i in range(len(pancakes)):
        if i == 0:
            s = 0
            if len(pancakes) > 0:
                sCurrent = pancakes[0][0] * pancakes[0][0] * math.pi + 2.0 * math.pi * pancakes[0][0] * pancakes[0][1]
                sNextTop = pancakes[1][0] * pancakes[1][0] * math.pi
                s = sCurrent - sNextTop
            if s < smallestSquare:
                smallestSquare = s
                smallestId = i
        else:
            s = 2.0 * math.pi * pancakes[i][0] * pancakes[i][1]
            if s < smallestSquare:
                smallestSquare = s
                smallestId = i

    del pancakes[smallestId]
    square -= smallestSquare
'''--------------------------------------'''

'''--------------Main block--------------'''
readInput()  # Read the whole input data input
testsCount = int(readNextLine())  # Read the tests count

for n in range(testsCount):
    print n + 1
    splitWords = readNextLine().split()

    allPancakes = int(splitWords[0]);
    usePancakes = int(splitWords[1]);

    '''Do something with data'''
    cleanUpLines()
    for i in range(allPancakes):
        addLine(readNextLine())

    solver()
    '''----------------------'''
    out_lines.append("Case #" + str(n + 1) + ": " + str(square))  # Save data result

saveOutput()  # Save the whole output data input
'''--------------------------------------'''