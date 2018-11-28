#!/usr/bin/python
# -*- encoding: utf-8 -*-

import sys
import math
import psyco

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
        l = readnumbers(self.dataset_stream)
        self.N = l[0]
        self.M = l[1]
        self.A = l[2]
    
    def printcase(self):
        print "Case #%d" % self.caseno
        print "N =", self.N, "M =", self.M, "Area =", self.A
        pass
    
    def solve(self):
        N = self.N
        M = self.M
        A = self.A
        self.solution = "a"
        if N * M < A:
            self.solution = "IMPOSSIBLE"

        self.solution = "IMPOSSIBLE"
        x1 = 0
        y1 = 0
        for x2 in range(0, N+1):
            for y2 in range(0, M+1):
                for x3 in range(0, N+1):
                    for y3 in range(0, M+1):
                        S2 = x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)
                        if S2 == A:
                            self.solution = "%d %d %d %d %d %d" % \
                                            (x1, y1, x2, y2, x3, y3)
                            return
        
    def printsolution(self):
        sys.stdout.flush()
        print >>sys.stderr, "Case #%d:" % self.caseno, self.solution
        sys.stderr.flush()

if __name__ == '__main__':
    psyco.full()
    filename = sys.argv[1]
    s = Solution()
    s.main(filename)
