from sys import stdin, stdout

class Solver :

    def run(self, caseIndex) :
        self.input()
        self.exe()
        self.output(caseIndex)

    def input(self) :
        self.digits = [int(_) for _ in stdin.readline().strip()]

    def output(self, caseIndex) :
        stdout.write("Case #%d: " % caseIndex)
        isStart = True
        for d in self.digits :
            if d or not isStart :
                stdout.write("%d" % d)
                isStart = False
        stdout.write("\n")

    def exe(self) :
        l = len(self.digits)
        index = -1
        for i in range(1, l) :
            if self.digits[i] < self.digits[i - 1] :
                index = i
                break

        stIndex = 0
        if index >= 0 :
            for i in range(index - 1, 0, -1) :
                if self.digits[i] > self.digits[i - 1] :
                    stIndex = i
                    break
            self.digits[stIndex] -= 1
            for i in range(stIndex + 1, l) :
                self.digits[i] = 9

if __name__ == "__main__" :
    caseNum = int(stdin.readline())
    for caseIndex in range(1, caseNum + 1) :
        instance = Solver()
        instance.run(caseIndex)

