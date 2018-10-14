#!/usr/bin/python

# Run by:
#     cat input | c.py

import sys

l = sys.stdin.readline()
cases = int(l)

for i in range(cases):
    print 'Case #%d:' % (i+1,),

    l = sys.stdin.readline()
    K = int(l)
    
    cards = [0]*K
    for j in range(K):
        cards[j] = j+1
        
    positions = {}
    cur_pos = 0
    for j in range(K):
        cur_pos = (cur_pos + j) % len(cards)
        positions[cards.pop(cur_pos)] = j+1

    l = sys.stdin.readline()
    indices = [int(x) for x in l.split()]
    assert len(indices) == indices[0]+1
    for j in indices[1:]:
        print positions[j],
    print
