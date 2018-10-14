#!/usr/bin/env python
import sys

class TestCase():
    def __init__(self,S,Q):
        self.S = S
        self.Q = Q

    def whats_next(self,current):
        #search engine not in the remaining query list
        for s in self.S:
            if s not in self.Q:
                return s
        #furthest away in the query
        tmp = []
        for q in self.Q:
            if q not in tmp:
                tmp.append(q)
        if tmp[-1] != current:
            return tmp[-1]
        else:
            return tmp[-2]

    def optimize(self):
        """ Optimize search engines call """
        n_opt = 0
        out = False
        current_S = None
        while(out==False):
            current_S = self.whats_next(self.Q[0])
            for n,q in enumerate(self.Q):
                if q != current_S:
                    #finished?
                    if n == len(self.Q)-1:
                        out = True
                #change search engine
                else:
                    self.Q = self.Q[n:]
                    n_opt += 1
                    current_S = self.whats_next(q)
                    break
        return n_opt
    
if __name__ == '__main__':
    #read input
    inp = open(sys.argv[1])
    out = open('universe.out','w')
    n_cases = int(inp.readline().strip())
    for n in range(n_cases):
        #parsing
        nS = int(inp.readline().strip())
        S = [inp.readline().strip() for s in range(nS)]
        nQ = int(inp.readline().strip())
        Q = [inp.readline().strip() for q in range(nQ)]

        #do test case
        if len(Q) > 0:
            case = TestCase(S, Q)
            print >> out, 'Case #%i: %i' %(n+1, case.optimize())
        else:
            print >> out, 'Case #%i: %i' %(n+1, 0)
    out.close()
