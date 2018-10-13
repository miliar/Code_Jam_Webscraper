import sys
import numpy
import datetime

def flipPancakes(cakes, size):
    flips = 0
    pancakeBits = numpy.zeros(len(cakes))
    for i in range(len(cakes)):
        if cakes[i] == "+":
            pancakeBits[i] = 1
    for i in range(len(cakes)):
        if (i + size - 1) < len(cakes):
            if not pancakeBits[i]:
                flips += 1
                for j in range(size):
                    pancakeBits[i + j] = not pancakeBits[i + j]
    for bit in reversed(pancakeBits):
        if not bit:
            return 'IMPOSSIBLE'
    return flips

print (datetime.datetime.now())

inputFile = open('pancakeFlipper.input', 'r')

outputFile = open('pancakeFlipper.output', 'w')

numLines = int(inputFile.readline())

for i in range(0, numLines):
    num = inputFile.readline()
    input = num.split(" ")
    outputFile.write('%s%s%s%s\n' % ('Case #', (i + 1), ': ', flipPancakes(input[0], int(input[1]))))

    print(i)

print (datetime.datetime.now())