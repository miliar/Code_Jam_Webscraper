import sys
import re

class Solver:
    def compute(self):
        A = {}
        def recCompute(x, k, v, kv, count):
            count += 1
            for i in range(x - k + 1):
                c = v ^ (kv << i)
                if c in A[x][k] and A[x][k][c] <= count:
                    return
                A[x][k][c] = count
                recCompute(x, k, c, kv, count)
        for i in range(2, 11):
            x = int('1' * i, 2)
            A[i] = {}
            for j in range(2, i + 1):
                A[i][j] = { x: 0 }
                recCompute(i, j, x, int('1' * j, 2), 0)
        self.A = A
    def solve(self, params):
        self.compute()
        S, K = params.split()
        K = int(K)
        s = len(S)
        c = int(S.replace('+', '1').replace('-', '0'), 2)
        return self.A[s][K][c] if s in self.A and K in self.A[s] and c in self.A[s][K] else 'IMPOSSIBLE'

class Main:
    def __init__(self):
        self.io = InOut()
        self.solver = Solver()
        self.resultTemplate = 'Case #%s: %s'
    def printResult(self, result):
        self.io.write(self.resultTemplate % result)
    def readInput(self):
        return self.io.readline()
    def start(self):
        T = int(self.io.readline()) + 1
        for t in range(1, T):
            params = self.readInput()
            self.printResult((t, self.solver.solve(params)))

class InOut:
    def __init__(self, inFile=True, outFile=True):
        self.fin = open('test.in', 'r') if inFile else sys.stdin
        self.fout = open('test.out', 'w') if outFile else sys.stdout
    def __enter__(self):
        return self
    def __exit__(self):
        self.fin.close()
        self.fout.close()
    def write(self, *s, sep='', end='\n'):
        print(*s, sep=sep, end=end, file=self.fout)
    def readline(self):
        return self.fin.readline().rstrip()
    def read(self):
        return self.fin.read().rstrip()

Main().start()
