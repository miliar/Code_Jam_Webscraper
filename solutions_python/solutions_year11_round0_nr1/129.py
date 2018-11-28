#!/usr/bin/env python
from sys import stdin

class bot(object):
    def __init__(self):
        self.pos = 1
        self.last = 0

t = input()

for i in range(t):
    bots = { 'O': bot(), 'B': bot() }
    nmoves = 0
    
    for move in stdin.readline().strip().split()[1:]:
        if move == 'O' or move == 'B':
            cur = move
        else:
            newpos = int(move)
            nmoves += max(0, abs(bots[cur].pos - newpos) - (nmoves - bots[cur].last)) + 1
            bots[cur].pos = newpos
            bots[cur].last = nmoves
            
    print "Case #%d: %d" % (i+1, nmoves)