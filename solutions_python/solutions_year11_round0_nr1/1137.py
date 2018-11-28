#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import sys

class Robot(object):
    def __init__(self, name, l):
        self.name = name
        self.pos = 1
        self.obj = None
        self.obj_pos = None
        for i, p in enumerate(l):
            if p[0] == self.name:
                self.obj = p[1]
                self.obj_pos = i
                break

    def updateObj(self, l, i):
        self.obj = None
        self.obj_pos = None
        while i < len(l):
            p = l[i]
            if p[0] == self.name:
                self.obj = p[1]
                self.obj_pos = i
                break
            i += 1
        #print self.name, 'has new obj:', self.obj

    def move(self):
        if self.obj is None: return
        if self.pos > self.obj:
            #print self.name, 'move from', self.pos, 'to', self.pos - 1
            self.pos -= 1
        elif self.pos < self.obj:
            #print self.name, 'move from', self.pos, 'to', self.pos + 1
            self.pos += 1
#        else:
            #print self.name, 'stay at', self.pos

    def __str__(self):
        return '<Robot ' + self.name + ': ' + \
            str(self.pos) + ' -> ' + str(self.obj) + \
            '>'

def solve(l):
    robots = [Robot('O', l), Robot('B', l)]
    t = 0
    idx = 0
    #print
    while idx < len(l):
        name, pos = l[idx]
        #print 't =', t, 'step:',idx,':', name, pos
        for r in robots:
            if r.name == name and r.pos == pos:
                #print r.name, 'push', pos
                idx += 1
                #if idx == len(l): return t
                #name, pos = l[idx]
                r.updateObj(l, idx)
            else:
                r.move()
        t+=1
    return t

f = open(sys.argv[1])
cases = []
with f:
    nbcases = int(f.readline())
    for case in xrange(nbcases):
        l = f.readline().split()
        l.pop(0)
        positions = []
        for p in zip(*[l[i::2] for i in xrange(2)]):
            positions.append((p[0], int(p[1])))
        #print positions
        print 'Case #' + str(case + 1) + ':', solve(positions)


