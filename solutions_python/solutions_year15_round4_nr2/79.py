#! /usr/bin/python
import os
import pyximport

#pyximport.install()
#os.chdir(os.path.dirname(os.path.abspath(__file__)))


#from ExtSolve import *

inf = open('input.in')
inp = inf.read().split('\n')
inf.close()

def Solve(*args):
    N, V, C, v = args
    time = 0
    if len(filter(lambda x:x[1]==C,v))==0 and \
            (len(filter(lambda x:x[1]>C,v))==0 or len(filter(lambda x:x[1]<C,v))==0 ):
        return 'IMPOSSIBLE'
    if N == 1:
        return ('%16.8f'%(V/v[0][0])).strip()
    elif N == 2:
        if v[0][1] == v[1][1]:
            return ('%16.8f'%(V/(v[0][0]+v[1][0]))).strip()
        x, y = (V * (C-v[0][1])) / (v[1][0] * (v[1][1] - v[0][1])), \
                (V * (C-v[1][1])) / (v[0][0] * (v[0][1] - v[1][1]))
        if x < 0 or y < 0 :
            return 'IMPOSSIBLE'
        else:
            return ('%16.8f'%max(x,y)).strip()

T = int(inp.pop(0))
outf = open('output','w')
for i in range(T):
    N, V, C = [float(x) for x in inp.pop(0).split(' ')]
    N = int(N)
    v = list()
    for j in range(N):
        v += [[float(x) for x in inp.pop(0).split(' ')]]
    outf.write('Case #%d: %s\n'%(i+1,Solve(N, V, C, v)))
outf.close()