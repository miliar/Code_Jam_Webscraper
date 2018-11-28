#! /usr/bin/python

__author__ = 'Thomas "noio" van den Berg'

### IMPORTS ###

import sys

# Shortcuts

### CONSTS ###


### FUNCTIONS ###

def can_have_score(score, total, maxdiff=2):
    remain = (total - score)
    if remain < 0:
        return False
    else:
        return remain / 2.0 >= (score - maxdiff)
    

### PROCESS INPUT FILE ###

f = open(sys.argv[1])
fout = open(sys.argv[1].replace('.in','.out'),'w')

T = int(f.readline())
for case in xrange(T):
    line = [int(d) for d in f.readline().split()]
    N = line[0]
    S = line[1]
    p = line[2]
    t = line[3:]
    
    can_have = 0
    only_surprising = 0
    for ti in t:
        if can_have_score(p, ti, maxdiff=1):
            can_have += 1
        elif can_have_score(p, ti):
            only_surprising += 1
    
    ans = can_have + min(only_surprising, S)
    print ans
    fout.write('Case #%d: %s\n'%(case+1,ans))
