from sys import stdin, stdout
import math

class Solver :
    
    def run(self, caseIndex) :
        self.input()
        self.exe()
        self.output(caseIndex)

    def input(self) :
        pancakes, strK = stdin.readline().split()
        self.pancakes = list(pancakes)
        self.k = int(strK)

    def output(self, caseIndex) :
        stdout.write("Case #%d: " % caseIndex)
        if self.flipCount < 0 :
            stdout.write("IMPOSSIBLE\n")
        else :
            stdout.write("%d\n" % self.flipCount)

    def exe(self) :
        self.flipCount = 0
        pancakeNum = len(self.pancakes)
        for i in range(pancakeNum) :
            if self.pancakes[i] == "-" :
                if i + self.k > pancakeNum :
                    self.flipCount = -1
                    return
                else :
                    self.flipCount += 1
                    for j in range(self.k) :
                        if self.pancakes[i + j] == "-" :
                            self.pancakes[i + j] = "+"
                        else :
                            self.pancakes[i + j] = "-"

if __name__ == "__main__" :
    caseNum = int(stdin.readline())
    instance = Solver()
    for caseIndex in range(caseNum) :
        instance.run(caseIndex + 1)

