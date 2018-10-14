#!/usr/bin/python
# -*- encoding: utf-8 -*-

import sys
import math
import psyco

class Solution:
    def main(self, filename):
        self.dataset_stream = open(filename, 'r')
        line = self.dataset_stream.readline()
        self.cases_left = int(line)
        print "File contains %d testcases." % (self.cases_left)

        self.init()

        self.caseno = 1
        while self.cases_left > 0:
            self.cases_left -= 1
            self.readcase()
            self.printcase()
            self.solve()
            self.printsolution()
            self.caseno += 1

    def init(self):
        self.tens = []
        p = 1
        for i in range(0, 41):
            self.tens.append(p)
            p *= 10

    def readcase(self):
        self.number_string = self.dataset_stream.readline().strip()

    def is_ugly(self, n):
        if n % 2 == 0:
            return True
        if n % 3 == 0:
            return True
        if n % 5 == 0:
            return True
        if n % 7 == 0:
            return True

        return False
    
    def printcase(self):
        print "Number:", self.number_string
        pass

    def variants(self, s):
        if len(s) == 1:
            return [(s, int(s))]

        if len(s) == 2:
            n1 = int(s[0])
            n2 = int(s[1])
            r = [(s, int(s)),
                 (s[0], n1+n2),
                 (s[0], n1-n2)]
            #print r
            return r

        variants = self.variants(s[1:])
        r = []
        for (n1, v) in variants:
            n = int(s[0])
            p = len(n1)
            x = self.tens[p]*n
            r.append((s[0] + n1, v + x))#; print r[-1]
            r.append((s[0], n + v))#; print r[-1]
            r.append((s[0], (v-int(n1)) + (n-int(n1))))#; print r[-1], v-int(n1), n-int(n1)

        return r

    def solve(self):
        variants = self.variants(self.number_string)
        count = 0
        #if len(variants) < 20:
        #print variants
        for (n, v) in variants:
            if self.is_ugly(v):
                #print "*", v
                count += 1

        self.solution = count

    def printsolution(self):
        sys.stdout.flush()
        print >>sys.stderr, "Case #%d: %d" % (self.caseno, self.solution)
        sys.stderr.flush()

if __name__ == '__main__':
    psyco.full()
    filename = sys.argv[1]
    s = Solution()
    s.main(filename)
