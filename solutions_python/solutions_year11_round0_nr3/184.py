#!/usr/bin/python
# -*- encoding: utf-8 -*-

import sys
import math
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
        N = int(self.dataset_stream.readline())
        C = readnumbers(self.dataset_stream)
        assert len(C) == N, "incorrect piles"
        self.C = C
    
    def printcase(self):
        #print self.C
        pass
    
    def solve(self):
        a = 0
        for x in self.C:
            a ^= x
        if a == 0:
            self.solution = sum(self.C) - min(self.C)
        else:
            self.solution = "NO"
        
    def printsolution(self):
        sys.stdout.flush()
        print >>sys.stderr, "Case #%d: %s" % (self.caseno, self.solution)
        sys.stderr.flush()

if __name__ == '__main__':
    #psyco.full()
    filename = sys.argv[1]
    s = Solution()
    s.main(filename)
