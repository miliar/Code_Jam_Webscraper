#!/usr/bin/python
# -*- encoding: utf-8 -*-

import sys
import math
import psyco

def readnumbers(f, dtype=int):
    return [dtype(x) for x in f.readline().strip().split()]

def pn(p, n):
    r = []
    for perm in p:
        for i in range(0, n+1):
            r.append(perm[0:i] + [n] + perm[i:])
    return r

def p2():
    return [[0,1],
            [1,0]]

def P(n):
    p = p2()
    for i in range(2, n):
        p = pn(p, i)
    return p

def permute(s, p):
    result = []
    for i in range(0,len(p)):
        result.append(s[p[i]])
    return ''.join(result)

def countgroups(s):
    c = 0
    ch = None
    for i in range(0, len(s)):
        if ch != s[i]:
            c += 1
            ch = s[i]
    return c

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
        self.k = readnumbers(self.dataset_stream)[0]
        self.s = self.dataset_stream.readline().strip()
    
    def printcase(self):
        pass

    def solve(self):
        k = self.k
        s = self.s
        sets = []
        for i in range(0, len(s)/k):
            sets.append(s[i*k:i*k+k])

        m = 10000000000
        for perm in P(k):
            r = ''.join([permute(set, perm) for set in sets])
            c = countgroups(r)
            #print r
            if c < m:
                m = c

        self.solution = m
        
    def printsolution(self):
        sys.stdout.flush()
        print >>sys.stderr, "Case #%d: %d" % (self.caseno, self.solution)
        sys.stderr.flush()

if __name__ == '__main__':
    psyco.full()
    filename = sys.argv[1]
    s = Solution()
    s.main(filename)
