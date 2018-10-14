#!/usr/bin/python
# -*- encoding: utf-8 -*-

import sys
import math
import psyco

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

def insert(tree, path, mark=False):
    if len(path) == 0:
        return
    if path[0] not in tree:
        tree[path[0]] = [mark, {}]
    insert(tree[path[0]][1], path[1:], mark)

def count(tree):
    sum = 0
    for path, (mark, subtree) in tree.iteritems():
        if not mark:
            sum += 1
        if subtree:
            sum += count(subtree)
    return sum

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
        tree = {}
        self.N, self.M = readnumbers(self.dataset_stream)
        for i in xrange(0, self.N):
            path = self.dataset_stream.readline().strip()
            parts = path.split('/')[1:]
            insert(tree, parts, True)
        for i in xrange(0, self.M):
            path = self.dataset_stream.readline().strip()
            parts = path.split('/')[1:]
            insert(tree, parts, False)

        self.tree = tree
    
    def printcase(self):
        #print repr(self.tree)
        pass
    
    def solve(self):
        self.answer = count(self.tree)
        
    def printsolution(self):
        sys.stdout.flush()
        print >>sys.stderr, "Case #%d: %s" % (self.caseno, self.answer)
        sys.stderr.flush()

if __name__ == '__main__':
    psyco.full()
    filename = sys.argv[1]
    s = Solution()
    s.main(filename)
