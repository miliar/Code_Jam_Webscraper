'''
Created on 12/04/2014

@author: luis
'''

class Case ():
    def __init__(self, caso, firstAnswer, firstSet, secondAnswer, secondSet):
        self.caso = int(caso+1)
        self.firstAnswer=firstAnswer
        self.firstSet = firstSet
        self.secondAnswer=secondAnswer
        self.secondSet = secondSet
        self.solution = []

    def resuelve(self):
        for i in self.firstSet:
            if i in self.secondSet:
                self.solution.append(i)
        if len(self.solution) == 1:
            outfile.write("Case #"+str(self.caso)+": %s \n" % self.solution[0])
        elif len(self.solution) >1 :
            outfile.write("Case #"+str(self.caso)+": Bad magician! \n")
        elif len(self.solution) == 0:
            outfile.write("Case #"+str(self.caso)+": Volunteer cheated! \n")



def getRow (set, row):
    return set[row-1]

infile = open('A-small-attempt1.in', 'r')
outfile = open('output.txt', 'w')
caseNumbers = int(infile.readline())
for i in range(caseNumbers):
    firstAnswer = int(infile.readline())
    firstSet = []
    secondSet = []
    for j in range (4):
        firstSet.append(infile.readline().split())
    secondAnswer = int(infile.readline())
    for k in range (4):
        secondSet.append(infile.readline().split())

    case = Case(i, firstAnswer, getRow (firstSet,firstAnswer), secondAnswer,
                getRow(secondSet, secondAnswer))

    case.resuelve()

outfile.close()
infile.close()