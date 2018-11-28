#!/usr/bin/python
# -*- encoding: utf-8 -*-

import sys
import math

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
        l = self.dataset_stream.readline().strip().split()
        self.P = int(l[0])
        self.K = int(l[1])
        self.L = int(l[2])
        self.alphabet = []
        l = self.dataset_stream.readline().strip().split()
        n = 0
        for f in l:
            self.alphabet.append((n, int(f)))
            n += 1
        assert len(self.alphabet) == self.L, "error reading frequences"
    
    def printcase(self):
        print "Case #%d:" % self.caseno
        print "Letters per key (P):", self.P
        print "Keys (K):", self.K
        print "Alphabet size (L):", len(self.alphabet)
        #print "Alphabet frequences:", self.alphabet
    
    def solve(self):
        self.alphabet.sort(lambda x, y: -cmp(x[1], y[1]))
        #print "Sorted alphabet:", self.alphabet

        N = 0
        presses = 1
        keys_used = 0
        for (letter, freq) in self.alphabet:
            keys_used += 1
            N += freq * presses
            if keys_used == self.K:
                presses += 1
                keys_used = 0

        self.solution = N
        
    def printsolution(self):
        sys.stdout.flush()
        print >>sys.stderr, "Case #%d: %d" % (self.caseno, self.solution)
        sys.stderr.flush()

if __name__ == '__main__':
    filename = sys.argv[1]
    s = Solution()
    s.main(filename)
