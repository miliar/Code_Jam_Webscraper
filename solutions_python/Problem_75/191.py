#!/usr/bin/python
# -*- encoding: utf-8 -*-

import sys
import math
from pprint import pprint
#import psyco

def readnumbers(f, dtype=int):
    return [dtype(x) for x in f.readline().strip().split()]

class Solution:
    def main(self, filename):
        self.dataset_stream = open(filename, 'r')
        line = self.dataset_stream.readline()
        self.cases_left = int(line)
        print "File contains %d testcases." % (self.cases_left)

        self.caseno = 1
        while self.cases_left > 0:
            self.cases_left -= 1
            self.readcase()
            self.printcase()
            self.solve()
            self.printsolution()
            self.caseno += 1

    def readcase(self):
        parts = self.dataset_stream.readline().split()
        C = int(parts[0])
        parts = parts[1:]
        rules = {}
        for i in xrange(C):
            a,b,p = parts[0]
            parts = parts[1:]
            rules[(a,b)] = p
            rules[(b,a)] = p

        D = int(parts[0])
        parts = parts[1:]
        opposing = set()
        for i in xrange(D):
            a, b = parts[0]
            parts = parts[1:]
            opposing.add((min(a,b), max(a,b)))

        N = int(parts[0])
        S = parts[1]
        assert len(S) == N, "incorrect invoke string"

        self.rules = rules
        self.opposing = opposing
        self.S = S
    
    def printcase(self):
        pass
        #print "Rules:"
        #pprint(self.rules)
        #pprint(self.opposing)
        #print self.S

    def transform(self, current):
        opposing = self.opposing
        rules = self.rules        
        while len(current) > 1:
            if len(current) > 1:
                k = (current[-1], current[-2]) 
                if k in rules:
                    current = current[:-2]
                    current.append(rules[k])
                else:
                    break
        for a, b in opposing:
            if (a in current) and (b in current):
                current = []
                break                
        return current
    
    def solve(self):
        current = []
        for E in self.S:
            current.append(E)
            current = self.transform(current)
        self.result = "[" + ', '.join(current) + "]"
        
    def printsolution(self):
        sys.stdout.flush()
        print >>sys.stderr, "Case #%d: %s" % (self.caseno, self.result)
        sys.stderr.flush()

if __name__ == '__main__':
    #psyco.full()
    filename = sys.argv[1]
    s = Solution()
    s.main(filename)
