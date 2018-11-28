from sys import stdin, stdout
import math

class Solver :

    def run(self, caseIndex) :
        self.input()
        self.calculate()
        self.output(caseIndex)

    def input(self) :
        self.N, self.K = (int(_) for _ in stdin.readline().split())
        self.cakes = []
        for i in range(self.N) :
            self.cakes.append(list(int(_) for _ in stdin.readline().split()))

    def calculate(self) :
        maxS = 0
        for i in range(self.N) :
            baseR = self.cakes[i][0]
            baseH = self.cakes[i][1]

            choices = []
            for j in range(self.N) :
                if j != i and self.cakes[j][0] <= baseR :
                    r = self.cakes[j][0]
                    h = self.cakes[j][1]
                    choices.append(2 * r * h)

            if len(choices) >= self.K - 1 :
                choices.sort(reverse = True)
                s = baseR * baseR + 2 * baseR * baseH
                for j in range(self.K - 1) :
                    s += choices[j]
                maxS = max(maxS, s)
        self.result = maxS * math.acos(0) * 2

    def output(self, caseIndex) :
        stdout.write("Case #%d: %.9f\n" % (caseIndex, self.result))

if __name__ == "__main__" :
    caseNum = int(stdin.readline())
    for caseIndex in range(1, caseNum + 1) :
        instance = Solver()
        instance.run(caseIndex)

