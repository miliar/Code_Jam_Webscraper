#!/usr/bin/python

import sys
import os

def main(inputfile):
    f = open(inputfile)
    
    lines = iter(map(lambda line: line.rstrip("\n"), f.readlines()))

    L, D, N = map(int, lines.next().split())
    words = [lines.next() for i in xrange(0, D)]
    cases = [lines.next() for i in xrange(0, N)]
    
    solver = Solver(L, D, N, words)
    
    for i, case in enumerate(cases):
        print "Case #%i: %i" % (i + 1, solver.solve(case))
    
class Solver():
    def __init__(self, L, D, N, words):
        self.L, self.D, self.N = L, D, N
        self.words = words
        
    def legals(self, case):
        k = 0
        m = -1
        while k < len(case):
            if case[k] == '(':
                m = k
            elif case[k] == ')':
                yield case[m + 1:k]
                m = -1
            elif m == -1:
                yield case[k]
            k += 1

        
    def solve(self, case):
        W = [i for i in xrange(0, self.D)]
        for i, legals in enumerate(self.legals(case)):
            dels = []
            for w in W:
                if not self.words[w][i] in legals:
                    dels.append(w)
            for w in dels:
                W.remove(w)
        return len(W)

if __name__ =='__main__':
    if len(sys.argv) < 2:
        print "Usage: %s filename" % os.path.basename(sys.argv[0])
    else:
            main(sys.argv[1])
