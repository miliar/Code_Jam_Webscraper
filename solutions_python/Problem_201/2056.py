import sys

class Solver:
    def recCompute(self, n):
        def getKey(x):
            return -(x[0] + x[1])
        if n in self.A:
            return self.A[n]
        else:
            d = n//2
            if n % 2 == 0:
                self.A[n] = [(d, d-1)]
                if d > 0:
                    self.A[n].extend(self.recCompute(d))
                if d > 1:
                    self.A[n].extend(self.recCompute(d-1))
            else:
                self.A[n] = [(d, d)]
                if d > 0:
                    self.A[n].extend(self.recCompute(d))
                    self.A[n].extend(self.recCompute(d))
            self.A[n] = sorted(self.A[n], key=getKey)
            return self.A[n]

    def computeAll(self):
        def getKey(x):
            return -(x[0] + x[1])
        A = { 1: [(0,0)] }
        for i in range(2,1001):
            d = i//2
            if i % 2 == 0:
                A[i] = [(d, d-1)]
                if d > 0:
                    A[i].extend(A[d])
                if d > 1:
                    A[i].extend(A[d-1])
            else:
                A[i] = [(d, d)]
                if d > 0:
                    A[i].extend(A[d])
                    A[i].extend(A[d])
            A[i] = sorted(A[i], key=getKey)
        self.A = A
    def solve(self, params):
        N,K = [int(x) for x in params.split()]
        return ' '.join([str(x) for x in self.recCompute(N)[K-1]])

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
        self.solver.computeAll()
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
