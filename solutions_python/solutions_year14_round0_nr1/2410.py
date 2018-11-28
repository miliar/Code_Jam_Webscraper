import itertools
import math
import operator

class MagicTrick:

    def __init__(self):
        self.inputFile = open('input.txt','r')
        self.outputFile = open('output.txt','w')
        numTestCases = int(self.inputFile.readline())
        print 'numTestCases', numTestCases
        for testCase in range(0, numTestCases):
            self.testCase = testCase+1
            self.cases = []
            for i in range(0, 2):
                case = self.getCase()
                self.cases.append(case)
            self.solveCases()

    def getCase(self):
        answer = int(self.inputFile.readline())
        grid = self.getGrid()
        return {'answer': answer, 'grid': grid}

    def getGrid(self):
        grid = []
        for i in range(0, 4):
            gridLine = [int(x) for x in self.inputFile.readline().split(' ')]
            grid.append(gridLine)
        return grid

    def solveCases(self):
        firstSet = set(self.cases[0]['grid'][self.cases[0]['answer']-1])
        secondSet = set(self.cases[1]['grid'][self.cases[1]['answer']-1])
        commonSet = firstSet & secondSet

        if len(commonSet) == 1:
            self.answer = commonSet.pop()
        elif len(commonSet) > 1:
            self.answer = 'Bad magician!'
        elif len(commonSet) == 0:
            self.answer = 'Volunteer cheated!'

        self.printAnswer()

    def printAnswer(self):
        outputString = 'Case #%d: %s\n'%(self.testCase,self.answer)
        self.outputFile.write(outputString)
        print outputString

if __name__ == '__main__':
    magicTrick = MagicTrick()