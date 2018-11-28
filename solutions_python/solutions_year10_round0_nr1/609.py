#!/usr/bin/python
# -*- encoding: utf-8 -*-

import sys
import math
#import psyco

def readnumbers(f, dtype=int):
    return [dtype(x) for x in f.readline().strip().split()]

def int2bin(n):
    rc = ''
    if n < 0: raise ValueError("must be a positive integer")
    if n == 0: return '0'
    while n > 0:
        rc = str(n % 2) + rc
        n = n >> 1
    return rc

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
        self.N, self.K = map(int, self.dataset_stream.readline().split())
    
    def printcase(self):
        print "%d snapper, %d clicks" % (self.N, self.K)
    
    def solve(self):
        on_mask = 2**(self.N)-1
        cutoff = ~((0xffffffff << (self.N))) & 0xffffffff
        state = self.K
        print "on mask: %s, cutoff: %s" % (int2bin(on_mask), int2bin(cutoff))
        print "after %d snaps: state=%s, state&cutoff = %s" % (self.K, int2bin(state), int2bin(state & cutoff))
        self.answer = (state & cutoff == on_mask) and "ON" or "OFF"
        
    def printsolution(self):
        sys.stdout.flush()
        print >>sys.stderr, "Case #%d: %s" % (self.caseno, self.answer)
        sys.stderr.flush()

if __name__ == '__main__':
    #psyco.full()
    filename = sys.argv[1]
    s = Solution()
    s.main(filename)
