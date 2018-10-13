from sys import stdin, stdout
import math

class Solver :

    def run(self, caseIndex) :
        self.input()
        self.calculate()
        self.output(caseIndex)

    def input(self) :
        self.actNum1, self.actNum2 = (int(_) for _ in stdin.readline().split())
        self.acts = []
        for i in range(self.actNum1) :
            st, ed = (int(_) for _ in stdin.readline().split())
            self.acts.append((st, ed, 0))
        for i in range(self.actNum2) :
            st, ed = (int(_) for _ in stdin.readline().split())
            self.acts.append((st, ed, 1))

    def calculate(self) :
        self.acts.sort()
        intervals = [[] for i in range(2)]
        remainTimes = [720, 720]
        lastSt, lastEd, lastName = self.acts[-1]
        lastEd -= 24 * 60
        self.count = 0
        for st, ed, name in self.acts :
            remainTimes[name] -= ed - st
            if name == lastName :
                intervals[name].append(st - lastEd)
                self.count += 2
            else :
                self.count += 1
            lastSt = st
            lastEd = ed
            lastName = name

        intervals[0].sort()
        intervals[1].sort()

        for name in range(2) :
            for time in intervals[name] :
                if time <= remainTimes[name] :
                    remainTimes[name] -= time
                    self.count -= 2
                else :
                    break

    def output(self, caseIndex) :
        stdout.write("Case #%d: %d\n" % (caseIndex, self.count))

if __name__ == "__main__" :
    caseNum = int(stdin.readline())
    for caseIndex in range(1, caseNum + 1) :
        instance = Solver()
        instance.run(caseIndex)

