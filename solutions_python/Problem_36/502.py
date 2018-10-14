#!/usr/bin/python
import re

FILE='C-small-attempt0'

SENTENCE = 'welcome to code jam'
def solve(caseidx, idx):
    global total
    global case
    tempidx = caseidx
    cur = SENTENCE[idx]
    lencase = len(case)
    while tempidx < lencase:
        if cur == case[tempidx]:
            if idx == 18:
                total += 1
            else:
                solve(tempidx+1, idx+1)
        tempidx += 1
    return

def solveiter():
    global total
    global case
    pos = []
    next = 0
    lensentence = len(SENTENCE)
    lencase = len(case)
    
    # Initialization of positions
    found = 0
    for i in xrange(lensentence):
        #print "i: " + str(i)
        for j in xrange(next, lencase):
            #print "j: " + str(j)
            #print "SENTENCE[i]: " + str(SENTENCE[i])
            #print "case[j]: " + str(case[j])
            if SENTENCE[i] == case[j]:
                pos.append(j)
                next = j+1
                found = 1
                break
        if not found:
            return
        else:
            found = 0

    total = 1
    #print "Init pos: " + str(pos)
    
    # Search for all combinations
    idx = lensentence - 1
    found = 0
    exit = 0
    while 1:
        found = 0
        for i in xrange(pos[idx]+1, lencase):
            if SENTENCE[idx] == case[i]:
                found = 1
                pos[idx] = i
                if idx == lensentence-1:
                    total += 1
                else:
                    idx += 1
                    pos[idx] = pos[idx-1]
                    break
        if not found:
            if idx == 0:
                break
            else:
                idx -= 1            
    return

def solveiteropt():
    global total
    global case
    pos = []
    let = []
    next = 0
    lensentence = len(SENTENCE)
    lencase = len(case)
    
    # Store letter positions
    next = 0
    for i in xrange(lensentence):
        tmp = []
        for j in xrange(next, lencase):
            if SENTENCE[i] == case[j]:
                tmp.append(j)
        let.append(tmp)
        if len(tmp) == 0:
            return
        else:
            next = tmp[0]+1
    #print str(let)
    
    # Initialization of positions
    for i in xrange(lensentence):
        pos.append(let[i][0])
    total = 1
    #print str(pos)
    
    # Search for all combinations
    idx = lensentence - 1
    found = 0
    while 1:
        found = 0
        for i in let[idx]:
            if i > pos[idx]:
                found = 1
                pos[idx] = i
                if idx == lensentence-1:
                    total += 1
                else:
                    idx += 1
                    pos[idx] = pos[idx-1]
                    break
        if not found:
            if idx == 0:
                break
            else:
                idx -= 1            
    return



# Input
fin = open(FILE + '.in', 'r')
fout = open(FILE + '.out', 'w')

opt = fin.readline()
N = int(opt) # Number of cases

cases = []
for i in range(N):
    cases.append(fin.readline().strip('\n'))

# Treat cases
for casenum, case in enumerate(cases):
    total = 0
    #solve(0, 0)
    #solveiter()
    solveiteropt()
    sol = ''
    for i in range(4-len(str(total))):
        sol += '0'
    sol += str(total)
    msg = "Case #" + str(casenum+1) + ": " + sol
    print msg
    fout.write(msg+'\n')