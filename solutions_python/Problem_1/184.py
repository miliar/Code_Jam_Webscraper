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
        self.engines = []
        n = int(self.dataset_stream.readline())
        for i in range(0, n):
            self.engines.append(self.dataset_stream.readline().strip())
        self.queries = []
        n = int(self.dataset_stream.readline())
        for i in range(0, n):
            self.queries.append(self.dataset_stream.readline().strip())
    
    def printcase(self):
        print "==================================="
        print "Search engines: %d" % len(self.engines)
        for engine in self.engines:
            print "    %s" % engine
        print "Queries: %d" % len(self.queries)
        for query in self.queries:
            print "    %s" % query

    def calc_distances(self, engines, queries):
        distance = {}
        for engine in engines:
            distance[engine] = 1000000
        for i in range(0, len(queries)):
            if 1000000 not in distance.values():
                break
            if distance[queries[i]] == 1000000:
                distance[queries[i]] = i
        d = [(e, distance[e]) for e in distance.keys()]
        d.sort(lambda x, y: -cmp(x[1], y[1]))
        return d
    
    def solve(self):
        engines = self.engines
        queries = self.queries

        self.switches = 0

        d = self.calc_distances(engines, queries)
        while len(queries) > 0:
            while len(queries) > 0 and queries[0] != d[0][0]:
                del queries[0]
            if len(queries) > 0:
                self.switches += 1
                d = self.calc_distances(engines, queries)
            
        
        
    def printsolution(self):
        sys.stdout.flush()
        print >>sys.stderr, "Case #%d: %d" % (self.caseno, self.switches)
        sys.stderr.flush()

if __name__ == '__main__':
    filename = sys.argv[1]
    s = Solution()
    s.main(filename)
