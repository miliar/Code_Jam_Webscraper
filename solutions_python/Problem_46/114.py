'''
Created on Sep, 2009

@author: gralfca
'''
try:
  import psyco
  psyco.full()
except ImportError:
  print >> sys.stderr, "No Psyco available ! To run faster, please, please install it!\n"


import sys
import re
import os
import time
from itertools import *
from pprint import pprint

if len(sys.argv) != 2:
    print 'specify input file'
    exit()

startTime = time.clock()

inputfile = sys.argv[1]
#inputfile = "/home/gralfca/dev/jam/round2/input.in"

fin = open(inputfile)
fout = open(os.path.splitext(inputfile)[0]+'.out','w')

def correct(mat, k):
    for i in xrange(len(mat)):
        if i < mat[i]-k: return False
    return True
    
def max(a,b):
    if a >b:
        return a
    return b
def swap(mat,i):
    mat[i], mat[i+1] = mat[i+1], mat[i]
    return mat

def encode(mat):
    if len(mat)==0: return ''
    return str(mat[0])+encode(mat[1:])

def countSwaps(mat, k):
    #print mat
    if correct(mat, k): return 0
    if known_sols.has_key(encode(mat)):
        return known_sols[encode(mat)]
    if mat[0]<=k:
        return countSwaps(mat[1:], k+1)
    minc = None
    for i in xrange(len(mat)-1):
        if mat[i]>mat[i+1]:
            a = mat*1
            swap(a,i)
            c = countSwaps(a, k)
            if minc == None: minc = c
            if c < minc: minc = c
    known_sols[encode(mat)] = minc + 1
    return minc + 1

def solve():
    global known_sols
    known_sols = {}
    N = int(fin.readline())
    mat = []
    for i in xrange (N):
        k = fin.readline().rfind('1')
        if k != -1:
            mat.append(k)
        else:
            mat.append(0)
    print>>fout,countSwaps(mat,0)

numCases = int(fin.readline())
for caseNo in range(numCases):
    print '\b'*10,100*caseNo/numCases,'%',
    print>>fout, 'Case #%s:'%(caseNo+1),
    solve()

fin.close()
fout.close()

print '\b'*10+'it took %.1fs'%(time.clock()-startTime)
