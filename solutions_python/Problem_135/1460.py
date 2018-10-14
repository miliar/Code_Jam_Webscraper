__author__ = 'ml'
import numpy as np


class cardGame:

    def __init__(self):
        self.state = 0
        self.board1 = []
        self.board2 = []

    def something(self,asdf):
        return 0

def parseOneDataPoint(lines, baseIndex):

    return 1

def solve(fname):
    data = np.loadtxt(fname,delimiter=' ')
    numCases = int(data[0,0])
    baseIndex = 1
    for case in range(0,numCases):
        guess1 = data[baseIndex,0]
        guess2 = data[baseIndex+5,0]

        board1Start = baseIndex + 0
        board2Start = baseIndex + 5

        #3 cases part lie - no overlap
        #  magician lie - overlap > 1
        # good overlap = 1

        overlap = np.intersect1d(data[board1Start+guess1,:],data[board2Start+guess2,:])

        if len(overlap) == 0:
            solution = 'Volunteer cheated!'
        if len(overlap) == 1:
            solution = str(int(overlap[0]))
        if len(overlap)  > 1:
            solution = 'Bad magician!'


        outFileName = fname + '.results'
        with open(outFileName, "a") as myfile:
            resultString =  "Case #" + str((case+1)) +": " + solution + '\n'
            myfile.write(resultString)
        baseIndex += 10

def solveMagiciain():
    files = ['A-small-attempt0.in','magician_test_input']
    for file in files:
        solution = solve(file)
        print(file, ' solved!')
    return 0


solveMagiciain()

