#!/usr/bin/python
# -*- encoding: utf-8 -*-

import sys
import math
#import psyco

def readnumbers(f, dtype=int):
    return [dtype(x) for x in f.readline().strip().split()]

class Solution:
    def main(self, filename):
        self.table = {}
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
        self.line = self.dataset_stream.readline().strip()
    
    def printcase(self):
        print self.line

    def count_for(self, line, search):
        key = (line, search)
        if key in self.table:
            return self.table[key]
        count = 0
        if len(search) == 1:
            count = line.count(search)
        elif len(search) > len(line):
            count = 0
        elif line == search:
            count = 1
        else:
            for i in xrange(0, len(line)-len(search)+1):
                ch = line[i]
                #print 'i:', i, 'ch:', ch
                if ch == search[0]:
                    #print "rec:", line[i+1:], "-", search[1:]
                    count += self.count_for(line[i+1:], search[1:])
                    count = count % 10000
                else:
                    continue

        #print "count_for '%s', '%s': %d" % (line, search, count)
        self.table[key] = count
        return count
    
    def solve(self):
        search = 'welcome to code jam'
        #search = 'hah'
        new = []
        for char in self.line:
            if char in search:
                new.append(char)

        line = ''.join(new)
        try:
            start_w = line.index(search[0])
            end_m = line.rindex(search[-1])
        except ValueError:
            self.count = 0
            return

        line = line[start_w:end_m+1]

        #print "minimized: %d -> %d" % (len(self.line), len(line))
        #self.count = 0
        self.count = self.count_for(line, search)
        return self.count
        
    def printsolution(self):
        sys.stdout.flush()
        print >>sys.stderr, "Case #%d: %04d" % (self.caseno, self.count)
        sys.stderr.flush()

if __name__ == '__main__':
#    psyco.full()
    filename = sys.argv[1]
    s = Solution()
    s.main(filename)
