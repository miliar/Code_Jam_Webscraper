#!/usr/bin/python
# -*- encoding: utf-8 -*-

import sys
import math
import commands

class Solution:
    def main(self, filename):
        self.dataset_stream = open(filename, 'r')
        line = self.dataset_stream.readline()
        self.cases_left = int(line)
        print "File contains %d testcases." % (self.cases_left)

        #self.load_primes()

        self.caseno = 1
        while self.cases_left > 0:
            self.cases_left -= 1
            self.readcase()
            self.printcase()
            self.solve()
            self.printsolution()
            self.caseno += 1

    def load_primes(self):
        f = open("primes.txt", 'r')
        self.primes = []
        for l in f:
            self.primes.append(int(l))
        f.close()
        print "loaded", len(self.primes), "primes"

    def readcase(self):
        l = self.dataset_stream.readline().strip().split()
        self.A = int(l[0])
        self.B = int(l[1])
        self.P = int(l[2])
    
    def printcase(self):
        print "A: %d, B: %d, P: %d" % (self.A, self.B, self.P)
    
    def solve(self):
        self.factors = []
        for n in range(self.A, self.B+1):
            f = [int(x) for x in commands.getoutput("factor %d" % n).strip().split()[1:]]
            self.factors.append(f)

        groups = []
        N = self.A
        extend = False
        for f in self.factors:
            print "factors for", N, ":", f
            N += 1
            for factor in f:
                extend = False
                if factor < self.P:
                    continue
                print "factor > P:", factor
                for g in groups:
                    if factor in g:
                        print "factor in group", g
                        extend = True
                        for x in f:
                            g.add(x)
                        print "extended group:", g
                    if extend:
                        break
            if not extend:
                print "new group:", set(f)
                groups.append(set(f))

        print "groups before reduction:", groups

        extend1 = True
        while extend1:
            extend1 = False
            groups2 = []
            for group in groups:
                extend = False
                for g2 in groups2:
                    i = g2.intersection(group)
                    if len(i) == 0:
                        continue
                    for n in i:
                        if n >= self.P:
                            extend = True
                            print g2, "will extend", group
                            break
                    if extend:
                        extend1 = True
                        g2 = g2.union(g)
                        break
                if not extend:
                    groups2.append(group)
            groups = groups2

        print groups
        self.solution = len(groups)
            
        
    def printsolution(self):
        sys.stdout.flush()
        print >>sys.stderr, "Case #%d: %d" % (self.caseno, self.solution)
        sys.stderr.flush()

if __name__ == '__main__':
    filename = sys.argv[1]
    s = Solution()
    s.main(filename)
