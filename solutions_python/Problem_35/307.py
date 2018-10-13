#!/usr/bin/python
# -*- encoding: utf-8 -*-

import sys
import math
#import psyco

def readnumbers(f, dtype=int):
    return [dtype(x) for x in f.readline().strip().split()]

def printmap(m):
    for row in m:
        print " ".join(('%05d' % n for n in row))

def validcoord(H, W, row, col):
    return row >= 0 and col >= 0 and row < H and col < W

def draincmp(a, b):
    ar, ac, av = a
    br, bc, bv = b
    if av != bv:
        return cmp(av, bv)

    if ar < br:
        return -1
    elif ar == br:
        if ac < bc:
            return -1
        else:
            return 1
    else:
        return 1

def draindir(m, row, col):
    H = len(m)
    W = len(m[0])
    possibilities = []
    for r, c in ((row-1, col),
                 (row+1, col),
                 (row, col-1),
                 (row, col+1)):
        if validcoord(H, W, r, c):
            possibilities.append((r, c, m[r][c]))
    if len(possibilities) == 0:
        return -1, -1
    possibilities.sort(draincmp)
    if possibilities[0][2] < m[row][col]:
        return possibilities[0][0], possibilities[0][1]
    else:
        return -1, -1

def drainable(m, row, col):
    return draindir(m, row, col) != (-1, -1)

def printdrain(m):
    for l in m:
        print " ".join(l)

class Solution:
    def main(self, filename):
        self.dataset_stream = open(filename, 'r')
        T = int(self.dataset_stream.readline())
        caseno = 0
        for i in xrange(0, T):
            caseno += 1
            H, W = readnumbers(self.dataset_stream)
            m = []
            for l in xrange(0, H):
                row = readnumbers(self.dataset_stream)
                assert len(row) == W
                m.append(row)

            print "-------------------------------------"
            print "map %02d cols x %02d rows:" % (W, H)
            printmap(m)
            d = []
            for r in xrange(0, H):
                d.append(['.'] * W)
            letters = [chr(n) for n in range(ord('a'), ord('z')+1)]
            letters.reverse()
            for r in range(0, H):
                for c in range(0, W):
                    #print "at", r, c, d[r][c]
                    if d[r][c] != '.':
                        #print "skip", r, c
                        continue
                    path = []
                    l = None
                    cr, cc = r, c
                    while True:
                        #print "cr, cc:", cr, cc, draindir(m, cr, cc)
                        path.append((cr, cc))
                        nr, nc = draindir(m, cr, cc)
                        if d[nr][nc] != '.':
                            l = d[nr][nc]
                            break
                        if not drainable(m, cr, cc):
                            break
                        cr, cc = nr, nc
                    #print "from", r, c, ":", path
                    if l is None:
                        l = letters.pop()
                    for rr, cc in path:
                        d[rr][cc] = l
                    #printdrain(d)
                    
            print >>sys.stderr, "Case #%d:" % caseno
            for r in xrange(0, H):
                print >>sys.stderr, ' '.join(d[r])
                    

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
#    psyco.full()
    filename = sys.argv[1]
    s = Solution()
    s.main(filename)
