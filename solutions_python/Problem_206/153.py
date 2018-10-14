from sys import stdin, stdout
import math

class Solver :

    def run(self, caseIndex) :
        self.input()
        self.calculate()
        self.output(caseIndex)

    def input(self) :
        self.D, self.N = (int(_) for _ in stdin.readline().split())
        self.horses = []
        for i in range(self.N) :
            self.horses.append((float(_) for _ in stdin.readline().split()))

    def calculate(self) :
        maxTime = 0.0
        for K, S in self.horses :
            maxTime = max(maxTime, (self.D - K) / S)
        self.result = self.D / maxTime

    def output(self, caseIndex) :
        stdout.write("Case #%d: %.8f\n" % (caseIndex, self.result))

if __name__ == "__main__" :
    caseNum = int(stdin.readline())
    for caseIndex in range(1, caseNum + 1) :
        instance = Solver()
        instance.run(caseIndex)

