from sys import stdin, stdout
import math

class Solver :

    def run(self, caseIndex) :
        self.input()
        self.calculate()
        self.output(caseIndex)

    def input(self) :
        self.N, self.P = [int(_) for _ in stdin.readline().split()]
        self.grams = [int(_) for _ in stdin.readline().split()]
        self.category = []
        for i in range(self.N) :
            self.category.append([int(_) for _ in stdin.readline().split()])

    def calculate(self) :
        self.available = []
        for i in range(self.N) :
            ava = []
            for j in range(self.P) :
                ava.append((max(1, math.ceil(self.category[i][j] / 1.1 / self.grams[i])), math.floor(self.category[i][j] / 0.9 / self.grams[i])))
            self.available.append(ava);

        if self.N == 1 :
            self.count = 0;
            for i in range(self.P) :
                l1, u1 = self.available[0][i];
                if u1 >= l1 :
                    self.count += 1
        else :
            self.used = [False for _ in range(self.P)];
            self.count = self.dfs(0)

    def dfs(self, index) :
        if index >= self.P :
            return 0
        l1, u1 = self.available[0][index];
        count = self.dfs(index + 1)
        if u1 >= l1 :
            for i in range(self.P) :
                if not self.used[i] :
                    l2, u2 = self.available[1][i]
                    if u2 >= l2 :
                        if not (u2 < l1 or l2 > u1) :
                            self.used[i] = True
                            tmp = self.dfs(index + 1) + 1
                            self.used[i] = False
                            if count < tmp :
                                count = tmp
        return count

    def output(self, caseIndex) :
        stdout.write("Case #%d: %d\n" % (caseIndex, self.count))

if __name__ == "__main__" :
    caseNum = int(stdin.readline())
    for caseIndex in range(1, caseNum + 1) :
        instance = Solver()
        instance.run(caseIndex)

