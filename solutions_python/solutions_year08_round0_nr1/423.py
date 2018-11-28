#!/usr/bin/env python 

from sys import argv

class Answer():
    def __init__(self, engines, queries):
        self.engines = engines
        self.queries = queries
        self._initialize()
        self.get_number_switches()

    def get_best_engine(self):
        top = self.queries[0]
        ls = []
        for eng in self.engines:
            if eng != top:
                ls.append(eng)
        depth = {}.fromkeys(ls, 0)
        for eng in ls:
            for  query in self.queries:
                if query != eng:
                    depth[eng] += 1
                else:
                    break
        current = ls[0]
        _max = depth[current]
        for  eng in ls:
            if depth[eng] > _max:
                current = eng
                _max = depth[current]
        self.current = current

    def _initialize(self):
        self.get_best_engine()
        self.switches = 0

    def get_number_switches(self):
        if len(self.queries) > 0:
            top = self.queries[0]
            if self.current != top:
                self.queries.pop(0)
            else:
                self.switches += 1
                self.get_best_engine()
            self.get_number_switches()
        else: return
            


fd = open(argv[1])
N  = int(fd.readline())
for  k in range(N):
    S = int(fd.readline())
    engines = []
    queries = []
    for i in range(S):
        engines.append(fd.readline().strip())
    Q = int(fd.readline())
    for i in range(Q):
        queries.append(fd.readline().strip())
    if Q == 0:
        print "Case #%i: 0" % (k + 1)
    else:
        answer = Answer(engines, queries)
        print "Case #%i: %i" % (k + 1, answer.switches)
