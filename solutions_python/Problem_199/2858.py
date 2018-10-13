# -*- coding: utf-8 -*-
"""
Created on Mon Mar 06 12:36:15 2017

@author: Ghomam
"""
import sys

#Open Test file
f = open(sys.argv[1])
data = f.readlines()
f.close()

# Input
tests = []
for t in data[1:]:
    temp = t.strip().replace('\n','')
    pile, K = temp.split(' ')
    pile = [ 0 if pile[i] == '-' else 1 for i in range(len(pile)) ]
    tests.append( [pile, int(K)] )

output = []
for test in tests:
    pile, K = test
    result = 0
    
    try:
        while True:
            i = pile.index(0)
            if len(pile[i:]) >= K:
                result += 1
                pile = pile[:i] + [ 0 if pile[i+n] else 1 for n in range(K) ] + pile[i+K:]
            else:
                result = 'IMPOSSIBLE'
                break
    except:
        pass
    output += [result]
    
#Output
result = open(sys.argv[1].replace('in', 'out'), 'w')
for i, r in enumerate(output):
    out = 'Case #{}: {}'.format(i+1, r)
    print out
    result.write(out+'\n')
result.close()