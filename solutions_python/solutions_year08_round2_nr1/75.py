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
        tmp = self.dataset_stream.readline().strip().split()
        self.n = int(tmp[0])
        self.A = int(tmp[1])
        self.B = int(tmp[2])
        self.C = int(tmp[3])
        self.D = int(tmp[4])
        self.x0 = int(tmp[5])
        self.y0 = int(tmp[6])
        self.M = int(tmp[7])
    
    def printcase(self):
        print "n: ", self.n
        print "A: ", self.A
        print "B: ", self.B
        print "C: ", self.C
        print "D: ", self.D
        print "x0: ", self.x0
        print "y0: ", self.y0
        print "M: ", self.M
        pass

    def build_grid(self):
        X = self.x0
        Y = self.y0
        grid = []
        grid.append((X, Y))
        for i in range(1, self.n):
            X = (self.A * X + self.B) % self.M
            Y = (self.C * Y + self.D) % self.M
            grid.append((X, Y))

        grid.sort(self.cmp_p)
        print repr(grid)

        self.grid = grid

    def cmp_p(self, a, b):
        if a[0] < b[0]:
            return -1
        elif a[0] > b[0]:
            return 1
        else:
            if a[1] < b[1]:
                return -1
            elif a[1] > b[1]:
                return 1
            else:
                return 0

    def solve(self):
        self.build_grid()
        grid = self.grid
        N = 0
        solutions = set()
        for n in range(0, len(grid)):
            for m in range(n+1, len(grid)):
                for k in range(m+1, len(grid)):
                    xc = self.grid[n][0] + self.grid[m][0] + self.grid[k][0]
                    yc = self.grid[n][1] + self.grid[m][1] + self.grid[k][1]
                    if xc % 3 != 0:
                        continue
                    if yc % 3 != 0:
                        continue

                    print n, m, k, xc/3, yc/3
                    N += 1

        self.solution = N
        
    def printsolution(self):
        sys.stdout.flush()
        print >>sys.stderr, "Case #%d: %d" % (self.caseno, self.solution)
        sys.stderr.flush()

if __name__ == '__main__':
    filename = sys.argv[1]
    s = Solution()
    s.main(filename)
