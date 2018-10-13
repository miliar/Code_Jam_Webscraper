#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from base import GcjSolver

class TerrainSolver(GcjSolver):
    casenum = 0

    def get_case(self):
        H, W = tuple([int(x) for x in self.get_line().split(" ")])
        matrix = [[[10001,'?'] for x in xrange(W+2)]]
        for i in xrange(H):
            line = self.get_line()
            matrix.append([[10001,'?']])
            matrix[i+1] += [[int(x), '?'] for x in line.split(' ') ]
            matrix[i+1].append([10001,'?'])
        matrix.append([[10001,'?'] for x in xrange(W+2)])
        case = (matrix, H, W)
        return case
    def solve(self, case):
        print "case", self.casenum
        self.casenum += 1
        self.matrix, H, W = case
        self.basins = 0
        for y in xrange(1,H+1):
            for x in xrange(1,W+1):
                self.process(x,y)

        s = "\n"
        for line in self.matrix[1:-1]:
            for elem in line[1:-1]:
                s+=elem[1]+" "
            s = s[:-1]
            s+="\n"
        return s[:-1]
    def process(self, x,y):
        if self.matrix[y][x][1] != '?':
            return
        #self.printt()
        #print "********f(%d,%d) = "%(x,y),self.matrix[y][x][0]
        next_coords = self.get_next(x,y)
        if next_coords:
            nx, ny = next_coords
            self.process(nx, ny)
            self.matrix[y][x][1] = self.matrix[ny][nx][1]
            #print "putting",self.matrix[ny][nx][1], "at", (x,y)
        else:
            #its a sink
            self.matrix[y][x][1] = self.get_new_char()
            #print "putting",self.matrix[y][x][1], "at", (x,y)
            return
    def get_next(self, x, y):
        if self.is_sink(x,y):
            return None

        minimum = min([self.matrix[y+dy][x+dx][0] for (dx,dy) in [(+1,0),(-1,0),(0,+1),(0,-1)]])
        for (dx,dy) in [(0,-1),(-1,0),(+1,0),(0,+1)]:
            if self.matrix[y+dy][x+dx][0] == minimum:
                #print "first minimun found was", (dx,y), (x,y), (dx+x,dy+y), self.matrix[y+dy][x+dx][0]
                return (x+dx, y+dy)

    def is_sink(self, x,y):
        #print "analizando si", (x,y),"de valor",self.matrix[y][x][0], "es sink..."
        this_level = self.matrix[y][x][0]
        #print "el valor de", (x,y), "es", this_level, self.matrix[y][x][0]
        for (dx,dy) in [(+1,0),(-1,0),(0,+1),(0,-1)]:
            if self.matrix[y+dy][x+dx][0] < this_level:
                #print "no lo es, pues f(%d,%d) = "%(x+dx,y+dy),self.matrix[y+dy][x+dx][0],"<",this_level
                return False
            else:
                pass
                #print "f(%d,%d) = "%(x+dx,y+dy),self.matrix[y+dy][x+dx][0], ">=", this_level
        #print (x,y), "es sink"
        return True
    def get_new_char(self):
        self.basins += 1
        return chr(ord('a')+self.basins -1)
    def printt(self):
        s0 = "\n"
        for line in self.matrix[1:-1]:
            for elem in line[1:-1]:
                s0+=str(elem[0])+" "
            s0 = s0[:-1]
            s0+="\n"
        s0 = s0[:-1]
        print s0


def main(program, name):
    s = TerrainSolver(name)
    s.run()


if __name__ == '__main__':
    reload(sys); sys.setdefaultencoding('utf-8')
    main(*sys.argv)