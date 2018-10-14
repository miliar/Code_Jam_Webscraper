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
roadDist = 0

horsesPos = []
horsesVel = []

def cleanUpLines():
    global horsesPos
    global horsesVel

    horsesPos = []
    horsesVel = []

def addLine(line):
    global horsesPos
    global horsesVel

    splitWords = line.split()
    horsesPos.append(float(splitWords[0]))
    horsesVel.append(float(splitWords[1]))

def newPosition(dt):
    global horsesPos
    global horsesVel

    for i in range(len(horsesPos)):
        horsesPos[i] = horsesPos[i] + dt * horsesVel[i]

    for i in range(len(horsesPos) - 1):
        n = len(horsesPos) - 1 - i
        if abs(horsesPos[n] - horsesPos[n - 1]) < 0.00000001:
            horsesVel[n - 1] = horsesVel[n]
            del horsesPos[n]
            del horsesVel[n]


def calculateHorses():
    global horsesPos
    global horsesVel

    horsesPos.reverse()
    horsesVel.reverse()

    lll = []
    for i in range(len(horsesPos)):
        lll.append([horsesPos[i], horsesVel[i]])

    lll.sort(key=lambda x: x[0])

    horsesPos = []
    horsesVel = []

    for i in range(len(lll)):
        horsesPos.append(lll[i][0])
        horsesVel.append(lll[i][1])

    print horsesPos
    print horsesVel

    t = 0.0

    if len(horsesPos) > 1:
        while horsesPos[0] < roadDist:
            smallestDt = (roadDist - horsesPos[0]) / horsesVel[0]

            for i in range(len(horsesPos) - 1):
                n = len(horsesPos) - 1 - i

                ds = horsesPos[n] - horsesPos[n - 1]
                dv = horsesVel[n - 1] - horsesVel[n]
                if ds > 0.00000001 and dv > 0.000000001:
                    dt = ds / dv
                    if dt > 0.0:
                        if dt < smallestDt:
                            smallestDt = dt

            newPosition(smallestDt)
            t += smallestDt


        print roadDist, horsesPos[0]
    else:
        t = (roadDist - horsesPos[0]) / horsesVel[0]

    vel = roadDist / t

    return vel
'''--------------------------------------'''

'''--------------Main block--------------'''
readInput()  # Read the whole input data input
testsCount = int(readNextLine())  # Read the tests count

for n in range(testsCount):
    print n + 1
    splitWords = readNextLine().split()


    roadDist = float(splitWords[0])
    rows = int(splitWords[1])
    '''Do something with data'''
    cleanUpLines()
    for i in range(rows):
        addLine(readNextLine())

    vel = calculateHorses()
    '''----------------------'''
    out_lines.append("Case #" + str(n + 1) + ": " + "{0:.8f}".format(vel))  # Save data result
    #for i in range(rows):
        #out_lines.append("".join(lines[i]))

saveOutput()  # Save the whole output data input
'''--------------------------------------'''
