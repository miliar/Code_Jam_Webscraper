#
#python 2.6

import math
import fractions

import time

INPUT_FILE = 'A-large.in'
OUT_FILE = 'A-large.out'
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
        N, K = [long(num) for num in strarray]
        matr = []
        for j in xrange(N):
            matr.append(rf.readline())
        yield N, K, matr


cachem = {}

def computey(dotarray,  N, K):
    rfind = False
    bfind = False
    for value, x, y in dotarray:
        if rfind and bfind: break
        if (value == 'R' and not rfind) or (value == 'B' and not bfind):
            find = True
            for i in xrange(K-1):
                if x+i+1 >= N: 
                    find = False
                    break
                if cachem.has_key( (x+i+1,  y) ):
                    if cachem[(x+i+1, y)] != value:
                        find = False
                        break
                else:
                    find = False
                    break
            if not find:
                find = True
                for i in xrange(K-1):
                    if x+i+1 >= N or y+i+1 >= N: 
                        find = False
                        break
                    if cachem.has_key( (x+i+1,  y+i+1) ):
                        if cachem[(x+i+1, y+i+1)] != value:
                            find = False
                            break       
                    else:
                        find = False
                        break
            if not find:
                find = True
                for i in xrange(K-1):
                    if y+i+1 >= N: 
                        find = False
                        break
                    if cachem.has_key( (x,  y+i+1) ):
                        if cachem[(x, y+i+1)] != value:
                            find = False
                            break
                    else:
                        find = False
                        break
                        
            if not find:
                find = True
                for i in xrange(K-1):
                    if x-i-1 < 0 or y+i+1 >= N: 
                        find = False
                        break
                    if cachem.has_key( (x-i-1,  y+i+1) ):
                        if cachem[(x-i-1, y+i+1)] != value:
                            find = False
                            break  
                    else:
                        find = False
                        break
                    
            if value == 'R': rfind = find
            if value == 'B': bfind = find
    if rfind and bfind:
        return 'Both'
    elif rfind:
        return 'Red'
    elif bfind:
        return 'Blue'
    else:
        return 'Neither'
    
def preprocess(N, K, matr):
    cachem.clear()
    dotarray = []
    for y in xrange(N):
        realx = N-1
        for x in xrange(N-1, -1, -1):
            if matr[y][x] != '.':
                cachem[(realx, y)] = matr[y][x] 
                dotarray.append((matr[y][x] , realx, y))
                realx -= 1
    return dotarray

caseIndex = 1
for N, K, matr in inputs():
    dotarray = preprocess(N, K, matr)
    y = computey(dotarray, N, K)
    wf.write('Case #{0}: {1}\n' .format(caseIndex,y)) 
#    print caseIndex, ':',  y
    caseIndex += 1

#print 'Done'
wf.close()
rf.close()
