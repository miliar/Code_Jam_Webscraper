# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 01:45:07 2015

@author: vbd
"""
ijk = { 'i' : 0, 'j' : 1, 'k' : 2 }

Q = { '1' : [  'i',  'j',  'k'],
      'i' : [ '-1',  'k', '-j'],
      'j' : [ '-k', '-1',  'i'],
      'k' : [  'j', '-i', '-1'],
     '-1' : [ '-i', '-j', '-k'],
     '-i' : [  '1', '-k',  'j'],
     '-j' : [  'k',  '1', '-i'],
     '-k' : [ '-j',  'i',  '1'] }

inp = raw_input()
T = int(inp)

for c in range(1,T+1) :
    inp = raw_input()
    LX = inp.split(' ')
    L, X = int(LX[0]), int(LX[1])
    s = raw_input().strip()
    assert L == len(s)
    S = s * X
    product = '1'
    soln = ['i', 'j', 'k']
    for ch in S:
        product = Q[product][ijk[ch]]
        if len(soln) == 0:
            continue
        if product == soln[0]:
            product = '1'
            tmp = soln.pop(0)
    if product == '1' and len(soln) == 0:
        print "Case #{0}: YES".format(c)
    else:
        print "Case #{0}: NO".format(c)
