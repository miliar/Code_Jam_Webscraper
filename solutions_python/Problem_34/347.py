#!/usr/bin/python
# -*- encoding: utf-8 -*-

import sys
import math
import psyco
import re

def readnumbers(f, dtype=int):
    return [dtype(x) for x in f.readline().strip().split()]

class Solution:
    def main(self, filename):
        self.dataset_stream = open(filename, 'r')
        L, D, N = readnumbers(self.dataset_stream)
        words = []
        cases = []
        for i in xrange(0, D):
            words.append(self.dataset_stream.readline().strip())
        for i in xrange(0, N):
            cases.append(self.dataset_stream.readline().strip())
        regexps = []
        for case in cases:
            groups = []
            current_group = []
            in_group = False
            for ch in case:
                if in_group:
                    if ch == '(':
                        raise ValueError
                    elif ch == ')':
                        groups.append(current_group)
                        in_group = False
                    else:
                        current_group.append(ch)
                else:
                    if ch == ')':
                        raise ValueError
                    elif ch == '(':
                        in_group = True
                        current_group = []
                    else:
                        groups.append([ch])
            regexp=''
            for charset in groups:
                regexp += '[%s]' % ''.join(charset)
            regexps.append(re.compile(regexp))

        print "Word length:", L
        print "Known words:", words
        print "Cases:", cases
        #print "Groups:", regexps
        for n, case in enumerate(regexps):
            count = 0
            for word in words:
                if case.match(word):
                    count += 1
            print >>sys.stderr, "Case #%d: %d" % (n+1, count)
            

    def readcase(self):
        pass
    
    def printcase(self):
        pass
    
    def solve(self):
        pass
        
    def printsolution(self):
        sys.stdout.flush()
        #print >>sys.stderr, "Case #%d: %d" % (self.caseno, self.switches)
        sys.stderr.flush()

if __name__ == '__main__':
    psyco.full()
    filename = sys.argv[1]
    s = Solution()
    s.main(filename)
