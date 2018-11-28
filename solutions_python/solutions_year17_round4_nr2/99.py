from sys import stdin, stdout
import math

class Solver :

    def run(self, caseIndex) :
        self.input()
        self.calculate()
        self.output(caseIndex)

    def input(self) :
        self.N, self.C, self.M = (int(_) for _ in stdin.readline().split())
        self.ts = [[] for _ in range(self.C)]
        for i in range(self.M) :
            s, c = (int(_) for _ in stdin.readline().split())
            self.ts[c - 1].append(s - 1)

    def calculate(self) :
        self.match1 = [None for _ in range(len(self.ts[1]))]
        self.ts[0].sort()
        self.ts[1].sort()
        self.result = 0
        self.unmatch = [[0 for _ in range(self.N)] for _ in range(self.C)]
        for i in range(len(self.ts[0])) :
            self.visited = [False for _ in range(len(self.ts[1]))]
            if self.dfs(i) :
                self.result += 1
            else :
                self.unmatch[0][self.ts[0][i]] += 1

        for i in range(len(self.ts[1])) :
            if self.match1[i] == None :
                self.unmatch[1][self.ts[1][i]] += 1

        self.prom = 0
        self.result += self.unmatch[0][0] + self.unmatch[1][0]
        for s in range(1, self.N) :
            match = min(self.unmatch[0][s], self.unmatch[1][s])
            self.result += match
            self.prom += match
            self.unmatch[0][s] -= match
            self.unmatch[1][s] -= match
            self.result += self.unmatch[0][s] + self.unmatch[1][s]

    def dfs(self, index) :
        for i in range(len(self.ts[1])) :
            if not self.visited[i] and self.ts[1][i] != self.ts[0][index] :
                self.visited[i] = True
                if self.match1[i] == None or self.dfs(self.match1[i]) :
                    self.match1[i] = index
                    return True
        return False

    def output(self, caseIndex) :
        stdout.write("Case #%d: %d %d\n" % (caseIndex, self.result, self.prom))

if __name__ == "__main__" :
    caseNum = int(stdin.readline())
    for caseIndex in range(1, caseNum + 1) :
        instance = Solver()
        instance.run(caseIndex)

