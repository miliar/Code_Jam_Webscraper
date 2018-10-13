#
#python 2.6

import math
import fractions

import time

INPUT_FILE = 'B-large.in'
OUT_FILE = 'B-large.out'
rf = file(INPUT_FILE)
wf = file(OUT_FILE, 'w')

caseNum = 0
def inputs():
    global caseNum
    if caseNum == 0:
        caseNum = rf.readline().strip()
        caseNum = int(caseNum)
    for i in xrange(caseNum):        
        strarray = rf.readline().strip().split()
        N, K, B, T = [int(num) for num in strarray]
        strarray = rf.readline().strip().split() 
        xarray = [int(num) for num in strarray]
        strarray = rf.readline().strip().split() 
        varray = [int(num) for num in strarray]        
        yield N, K, B, T, xarray, varray


def computey(N, K, B, T, xarray, varray):
    tarray = []
    for i in xrange(N):
        tarray.append( divmod(B-xarray[i], varray[i]) )
        
    
#    tmp = tarray[:]
#    tmp.sort(lambda x,y: cmp(x[0], y.lower()) )
#    if tmp[K-1] > T: 
#        return 'IMPOSSIBLE'
    
    s = 0
    curr = 0
    for i in xrange(N-1, -1, -1):
        if tarray[i][0] > T or (tarray[i][0] == T and tarray[i][1] != 0):
            s += K-curr
        else:
            curr += 1
            if curr >= K:
                break
    if curr < K:
        return 'IMPOSSIBLE'
    
    return s
    
caseIndex = 1
for N, K, B, T, xarray, varray in inputs():
    y = computey(N, K, B, T, xarray, varray)
    wf.write('Case #{0}: {1}\n' .format(caseIndex,y)) 
    print caseIndex, ':',  y
    caseIndex += 1

print 'Done'
wf.close()
rf.close()
