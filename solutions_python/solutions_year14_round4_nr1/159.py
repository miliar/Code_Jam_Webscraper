import os
import sys
import math
import re
import pdb

inf = open('input.txt')
inp = inf.read().split('\n')
inf.close()

result = []
T = int(inp.pop(0))
for i in range(0,T):
    disc = 0
    line = inp.pop(0)
    N, X = map(lambda x:int(x),line.split(' '))

    line = inp.pop(0)
    S = map(lambda x:int(x),line.split(' '))
    S.sort(reverse=True)

    while len(S) > 0:
        if len(S) == 1:
            disc += 1
            S.pop(0)
            continue
        two_file = False
        for i in range(1,len(S)):
            if S[i] + S[0] <= X:
                S.pop(i)
                S.pop(0)
                disc += 1
                two_file = True
                break
        if not two_file:
            S.pop(0)
            disc += 1
    result += [disc]

outf = open('output','w')
for i in range(0,T):
    outf.write('Case #%d: %s\n'%(i+1,result[i]))
outf.close()