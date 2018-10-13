#Munkres is BSD license at http://www.clapper.org/software/python/munkres/
#easy_install munkres

from munkres import Munkres

class Case:
    def __init__(self, s):
        self.size = int(s.read())
        self.v1 = map(int, s.read().split(" "))
        self.v2 = map(int, s.read().split(" "))

    def solve(self):
        matrix = [[0 for v in self.v1] for x in self.v2]
        for i in range(len(self.v1)):
            for j in range(len(self.v2)):
                matrix[i][j] = self.v1[i] * self.v2[j]
        m = Munkres()
        indexes = m.compute(matrix)
        total = 0
        for row, column in indexes:
            total += matrix[row][column]
        return "%d" % total        

class Contents:
    def __init__(self, f):
        self.data = [line.strip() for line in f]
        self.i = 0

    def read(self):
        return self.readList(1)[0]

    def readList(self, len):
        result = self.data[self.i : self.i + len]
        self.i += len
        return result

import sys
f = file(sys.argv[1])
s = Contents(f)
numCases = int(s.read())

for caseNum in range(numCases):
    case = Case(s)
    print "Case #%d: %s" % (caseNum + 1, case.solve())
