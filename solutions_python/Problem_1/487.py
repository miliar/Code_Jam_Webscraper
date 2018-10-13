import sys

sys.setrecursionlimit(1500)
class problem:
    def __init__(self, filename="sample.txt"):
        self.cases = []
        self.add_cases(filename)
    def add_cases(self,filename):
        import os,readline
        f = open(filename, "r")
        N = int(file.readline(f))
        global cases
        for X in range(N):
            z = case()
            z.S = int(file.readline(f)) # number of engines
            for b in range(z.S):
                z.engines.append(str(file.readline(f)[:-1])) # the engines
            z.Q = int(file.readline(f)) # number of queries
            for b in range(z.Q): 
                z.queries.append(str(file.readline(f)[:-1])) # the queries ( :-1 is used to get rid of newline)
            self.cases.append(z)
class case:
    def __init__(self):
        self.S = 0
        self.Q = 0
        self.engines = []
        self.queries = []
        self.path = []
        self.answer = None # number of search engine switches
    def brute_force(self):
        if self.answer is not None:
            print self.answer
        else: 
            def X(offset):   # search for paths through queries of length C, starting at offset position with engine E
                a = 0 # len(self.queries[offset:])
                best_engine = None
                for s in self.engines:
                    b = self.queries[offset:].count(s)
                    if b > 0:
                        c = self.queries[offset:].index(s)
                        if c > a:
                            a = c
                            best_engine = s
                    else:
                        a = -1
                        best_engine = s
                        break
                if a is -1:
                    self.path.append(best_engine)
                    self.answer = len(self.path) - 1
                    return
                else:
                    offset += a
                    self.path.append(best_engine)
                    X(offset)
            X(0)
x = problem("large1")
for i in range(len(x.cases)):
    a = x.cases[i].brute_force()
    print "Case #" + str(i+1) + ": " + str(x.cases[i].answer)

