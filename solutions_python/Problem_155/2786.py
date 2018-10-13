
import sys

class Problem:
    def __init__(self):
        pass

    def read_(self):
        return self.inFile_.readline()

    def write_(self, line):
        self.outFile_.write(line + "\n")

    def solve(self, filename):
        self.inFile_ = open(filename + ".in", "r")
        self.outFile_ = open(filename + ".out", "w")
        N = int(self.read_())
        for n in range(N):
            line = self.solveCase_()
            self.write_("Case #%d: " % (n+1) + line)

    def solveCase_(self):
        result = 0
        line = self.read_().split(" ")
        sMax = int(line[0])
        data = line[1]
        currentShy = 0

        for i in range(len(data)-1):
            if (currentShy >= i):
                currentShy += int(data[i]) 
            else:
                currentShy += int(data[i]) + 1
                result += 1
                
        result += max(sMax - currentShy, 0)

        return str(result)

problem = Problem()
problem.solve("A-large")
