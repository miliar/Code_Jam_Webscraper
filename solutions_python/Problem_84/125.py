#!/usr/bin/python
# -*- encoding: utf-8 -*-

import sys
import math
import numpy
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
        R, C = readnumbers(self.dataset_stream)
        board = numpy.zeros((R, C), 'i')
        for r in xrange(R):
            for c, t in enumerate(self.dataset_stream.readline().strip()):
                if t == '#':
                    board[r][c] = 1
        self.board = board
        self.R, self.C = R, C
    
    def printcase(self):
        print repr(self.board)
    
    def solve(self):
        R, C = self.R, self.C
        board = self.board
        def find_start(R, C, board):
            for r in xrange(R):
                for c in xrange(C):
                    if board[r][c] == 1:
                        return r, c
            return None, None

        r, c = find_start(R, C, board)
        self.answer = "Impossible"
        while (r is not None) and (c is not None):
            if r+1 >= R or c+1 >= C or \
                   (board[r  ][c  ] != 1) or \
                   (board[r+1][c  ] != 1) or \
                   (board[r+1][c+1] != 1) or \
                   (board[r  ][c+1] != 1):
                return
            board[r][c] = 2
            board[r][c+1] = 3
            board[r+1][c] = 3
            board[r+1][c+1] = 2
            r, c = find_start(R, C, board)

        has_1 = False
        has_2 = False
        for r in xrange(R):
            for c in xrange(C):
                if board[r][c] == 1:
                    has_1 = True
                elif board[r][c] > 2:
                    has_2 = True

        if not has_1:
            result = ''           
            for r in xrange(R):
                row = ''                
                for c in xrange(C):
                    if board[r][c] == 2:
                        row += '/'
                    elif board[r][c] == 3:
                        row += '\\'
                    else:
                        row += '.'
                result += row
                result += '\n'
            self.answer = result.strip()
        
        
    def printsolution(self):
        sys.stdout.flush()
        print >>sys.stderr, "Case #%d:\n%s" % (self.caseno, self.answer)
        sys.stderr.flush()

if __name__ == '__main__':
    #psyco.full()
    filename = sys.argv[1]
    s = Solution()
    s.main(filename)
