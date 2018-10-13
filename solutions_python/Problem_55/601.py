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
        self.R, self.k, self.N = readnumbers(self.dataset_stream)
        self.g = readnumbers(self.dataset_stream)
        assert len(self.g) == self.N
    
    def printcase(self):
        print "Rides: %d, size: %d; groups: %s" % (self.R, self.k, " ".join(map(str, self.g)))
    
    def solve(self):
        self.sum = 0
        for i in xrange(self.R):
            occupied = 0
            new_queue = []
            while len(self.g) > 0 and occupied + self.g[0] <= self.k:
                occupied += self.g[0]
                new_queue.append(self.g[0])
                self.g = self.g[1:]
            self.sum += occupied
            self.g.extend(new_queue)
        
    def printsolution(self):
        sys.stdout.flush()
        print >>sys.stderr, "Case #%d: %d" % (self.caseno, self.sum)
        sys.stderr.flush()

if __name__ == '__main__':
    #psyco.full()
    filename = sys.argv[1]
    s = Solution()
    s.main(filename)
