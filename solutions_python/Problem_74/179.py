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
        parts = self.dataset_stream.readline().split()
        N = int(parts[0])
        commands = []
        parts = parts[1:]
        for i in xrange(0, len(parts), 2):
            commands.append((parts[i], int(parts[i+1])))
        assert len(commands) == N, "wrong number of instructions"
        self.N = N
        self.commands = commands
    
    def printcase(self):
        print "%d commands" % (self.N)
    
    def solve(self):
        commands = self.commands

        xo = 1
        xb = 1
        t = 0

        def next_position(color, commands):
            for c, p in commands:
                if c == color:
                    return p
            return None

        next_O = next_position('O', commands)
        next_B = next_position('B', commands)

        print "time\tB[0]\tO[0]\txb\txo"
        while len(commands) > 0:
            who, pos = commands[0]
            t += 1            
            print "%d\t%s\t%s\t%d\t%d\t" % (t, next_O, next_B, xb, xo)

            O_busy = False
            B_busy = False

            if who == 'O' and xo == pos:
                print "O push"
                O_busy = True
                commands = commands[1:]
                next_O = next_position('O', commands)
            elif who == 'B' and xb == pos:
                print "B push"
                B_busy = True
                commands = commands[1:]
                next_B = next_position('B', commands)

            if not O_busy:
                if xo > next_O:
                    xo -= 1
                elif xo < next_O:
                    xo += 1

            if not B_busy:
                if xb > next_B:
                    xb -= 1
                elif xb < next_B:
                    xb += 1

        self.t = t
        
    def printsolution(self):
        sys.stdout.flush()
        print >>sys.stderr, "Case #%d: %d" % (self.caseno, self.t)
        sys.stderr.flush()

if __name__ == '__main__':
    #psyco.full()
    filename = sys.argv[1]
    s = Solution()
    s.main(filename)
