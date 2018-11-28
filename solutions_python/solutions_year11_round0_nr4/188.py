#!/usr/bin/python
# -*- encoding: utf-8 -*-

import sys
import math
import numpy
#import psyco

def readnumbers(f, dtype=int):
    return [dtype(x) for x in f.readline().strip().split()]

def rearrange_paired(S):
    swaps = 0
    for i in xrange(1, len(S)):
        if S[i] == i:
            continue
        j = S[i]
        if S[j] == i:
            S[i] = i
            S[j] = j
            swaps += 1
    return swaps

def is_sorted(S):
    for i in xrange(1, len(S)):
        if S[i] != i:
            return False
    return True

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
        S = readnumbers(self.dataset_stream)
        assert len(S) == N, "incorrect array"
        self.S = S
    
    def printcase(self):
        #print "[" + ', '.join(str(x) for x in self.S) + "]"
        pass

    def solve(self):
        S = self.S
        swaps = 0
        for i in xrange(len(S)):
            if S[i] != i+1:
                swaps += 1
        self.swaps = swaps
        
    def printsolution(self):
        sys.stdout.flush()
        print >>sys.stderr, "Case #%d: %f" % (self.caseno, self.swaps)
        sys.stderr.flush()

if __name__ == '__main__':
    #psyco.full()
    filename = sys.argv[1]
    s = Solution()
    s.main(filename)
