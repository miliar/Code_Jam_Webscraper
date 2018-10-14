from sys import stdin, stdout
import math

class Solver :

    def run(self, caseIndex) :
        self.input()
        self.calculate()
        self.output(caseIndex)

    def input(self) :
        self.N, self.P = (int(_) for _ in stdin.readline().split())
        self.groups = (int(_) for _ in stdin.readline().split())

    def calculate(self) :
        count = [0 for _ in range(self.P)]
        for g in self.groups :
            count[g % self.P] += 1

        self.result = 0

        self.result += count[0];
        if self.P == 2 :
            self.result += math.ceil(count[1] / self.P)
        elif self.P == 3 :
            match = min(count[1], count[2])
            self.result += match
            count[1] -= match
            count[2] -= match
            self.result += math.ceil(count[1] / self.P)
            self.result += math.ceil(count[2] / self.P)
        elif self.P == 4 :
            match1 = min(count[1], count[3])
            self.result += match1
            count[1] -= match1
            count[3] -= match1

            match2 = int(count[2] / 2)
            self.result += match2
            count[2] = count[2] % 2

            if count[2] :
                if count[1] :
                    if count[1] >= 2 :
                        self.result += 1
                        count[1] -= 2
                        self.result += math.ceil(count[1] / self.P)
                    else :
                        self.result += 1
                elif count[3] :
                    if count[3] >= 2 :
                        self.result += 1
                        count[3] -= 2
                        self.result += math.ceil(count[3] / self.P)
                    else :
                        self.result += 1
                else :
                    self.result += 1
            else :
                if count[1] :
                    self.result += math.ceil(count[1] / self.P)
                elif count[3] :
                    self.result += math.ceil(count[3] / self.P)
                else :
                    pass

    def output(self, caseIndex) :
        stdout.write("Case #%d: %d\n" % (caseIndex, self.result))

if __name__ == "__main__" :
    caseNum = int(stdin.readline())
    for caseIndex in range(1, caseNum + 1) :
        instance = Solver()
        instance.run(caseIndex)

