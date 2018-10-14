import sys
from copy import deepcopy

maxint = 10001
letters = 'abcdefghijklmnopqrstuvwxyz'

def mark(h, w):
    wrapList = wrap(h, w)
    ori = deepcopy(wrapList)
    index = 0
    for i in range(1, h + 1):
        for j in range(1, w + 1):
            if str(wrapList[i][j]) in letters:
                continue                               
            a = visit(wrapList, ori, i, j, letters[index])
            if a == False:
                index = index + 1
    for row in range(1, h + 1):
        output = ""
        for col in range(1, w + 1):
            output = output + wrapList[row][col] + ' '
        print output            

def wrap(h, w):
    wrapList = []
    boundary = [maxint for i in range(0, w + 2)]
    wrapList.append(boundary)
    for i in range(1, h + 1):
        temp = [maxint]           
        temp.extend([int(item) for item in raw_input().split(' ')])
        temp.append(maxint)
        wrapList.append(temp)
    wrapList.append(boundary)
    return wrapList

def visit(aList, ori, i, j, label):
    sort = [ori[i-1][j], ori[i][j-1], ori[i][j+1], ori[i+1][j]]
    minimum = min(sort)    
    if aList[i][j] <= minimum: # a sink
        aList[i][j] = label
        return False
    chosen = -1    
    for m in range(4):
        if sort[m] == minimum:
            chosen = m
            break

    if chosen == 0:
        lb = str(aList[i-1][j])
        if lb in letters:
            aList[i][j] = lb
            return lb
        result = visit(aList, ori, i-1, j, label)
        if result != False:
            aList[i][j] = result
            return result

    if chosen == 1:
        lb = str(aList[i][j-1])
        if lb in letters:
            aList[i][j] = lb
            return lb
        result = visit(aList, ori, i, j-1, label)
        if result != False:
            aList[i][j] = result
            return result

    if chosen == 2:
        lb = str(aList[i][j+1])
        if lb in letters:
            aList[i][j] = lb
            return lb
        result = visit(aList, ori, i, j+1, label)
        if result != False:
            aList[i][j] = result
            return result

    if chosen == 3:
        lb = str(aList[i+1][j])
        if lb in letters:
            aList[i][j] = lb
            return lb
        result = visit(aList, ori, i+1, j, label)
        if result != False:
            aList[i][j] = result
            return result
    
    aList[i][j] = label
    return False
       
T = int(raw_input())
for i in range(T):
    print "Case #%s:" % (i+1)
    H, W = [int(item) for item in raw_input().split(' ')] 
    mark(H, W)



