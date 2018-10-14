#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Google CodeJam
Task  -

Solution by Joao Moreno <alph.pt@gmail.com> 2008

Usage: python [source_file] < [input_file] > [output_file]
"""

"""f(e,q) =
  0, |q| == 1 && e != q
  1, |q| == 1 && e == q
  f(e,q2), e != q
  min(f(ek,q2))+1, e == q"""


"""
1
5
Yeehaw
NSM
Dont Ask
B9
Googol
10
Yeehaw
Yeehaw
Googol
B9
Googol
NSM
B9
NSM
Dont Ask
Googol
"""

class SearchCentral(object):
    def __init__(self, engines):
        self.engines = engines
    
    def optimalSearch(self, queries):
        if len(queries) == 0:
            return 0        
        
        mem = []
        line = []
        
        # i, 1
        for i in range(len(self.engines)):
            if queries[0] == self.engines[i]:
                line.append(1)
            else:
                line.append(0)
        mem.append(line)
        
        # i, j
        for j in range(1,len(queries)):
            line = []
            for i in range(len(self.engines)):
                if queries[j] == self.engines[i]:
                    line.append(min(mem[j-1][:i] + mem[j-1][i+1:]) + 1)
                else:
                    line.append(mem[j-1][i])
            mem.append(line)
        
        return min(mem[-1])

if __name__ == '__main__':
    from codejam.io import Scanner
    s = Scanner()
    N = s.readInt()
    for i in range(1,N+1):
        S = s.readInt()
        engines = {}
        for j in range(S):
            engines[j] = s.readLine()
        
        Q = s.readInt()
        queries = []
        for j in range(Q):
            queries.append(s.readLine())
        
        print "Case #%i: %i" % (i, SearchCentral(engines).optimalSearch(queries))
