'''
Created on 2012-4-18

@author: hemnd
'''

def cal(A, B, Al):
    p = 1.0
    for i in range(0, A):
        p *= Al[i]
    mi = B + 2.0
    for i in range(0, A):
        luck = B - A + 2 * i + 1.0
        k = p * luck + (1.0 - p) * (luck + B + 1.0)
        if k < mi:
            mi = k
        p /= Al[-(i + 1)]
    return mi

inputFile = open('A-small-attempt0.in', 'r')
#inputFile = open('test.txt', 'r')
inputLines = inputFile.readlines()
inputFile.close()

T = int(inputLines[0])
outputLines = []

l = 1
for i in range(1, T + 1):
    args = inputLines[l].strip().split(' ')
    A = int(args[0])
    B = int(args[1])
    l += 1
    args = inputLines[l].strip().split(' ')
    Al = []
    for p in args:
        Al.append(float(p))
    l += 1
    outputLines.append('Case #%d: %.6f\n' % (i, cal(A, B, Al)))
    print outputLines[-1],

outputFile = open('A-S.out', 'w')
outputFile.writelines(outputLines)
outputFile.close()
