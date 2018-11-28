import psyco
psyco.full()

class Case:
    def __init__(self, s):
        self.k = int(s.read())
        self.string = s.read()
        
    def rle(self, string):
        rle = 1
        i = 1
        while i < len(string):
            if string[i] != string[i - 1]:
                rle += 1
            i += 1
        return rle
    
    def perms(self, list):
        if list == []:
            return [[]]
        return [[list[i]] + p for i in range(len(list)) for p in self.perms(list[:i] + list[i+1:])]

    def solve(self):
        mincount = 10000000
        klist = [i for i in range(self.k)]
        for perm in self.perms(klist):
            string2 = [char for char in self.string]
            for i in range(len(string2) / self.k):
                for j in range(self.k):
                    string2[self.k * i + j] = self.string[self.k * i + perm[j]]
            rlect = self.rle(string2)
            if rlect < mincount:
                mincount = rlect
        return "%d" % mincount

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
