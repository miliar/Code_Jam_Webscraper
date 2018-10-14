from datetime import datetime
import copy
import collections
import math
 
#Input
#fName = input('Enter Filename of Input:\n')
with open('test.in') as f:
    inp = [line.rstrip() for line in f]
    
#Output
proj = 'ihop '
timestamp = datetime.now().strftime("%H.%M.%S")
out = open(proj+timestamp+'.out', 'w')
 
#Problem
caseCount = int(inp[0])

for i in range(0,caseCount):
    lineNo = i * 2 + 1
    case = i +1
    
    diners = inp[lineNo]
    dinerQts = [int(j) for j in inp[lineNo+1].split()]
    most = max(dinerQts)
    best = most

    for tallestStack in range (2, most):
        moves = 0
        for diner in dinerQts:
            if(diner>tallestStack):
                 moves += math.ceil(diner / tallestStack) - 1
        if tallestStack+moves < best:
            best = tallestStack+moves
    out.write('Case #%d: %d\n'%(case,best))

out.close()
