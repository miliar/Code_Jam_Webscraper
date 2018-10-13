import sys
import fileinput
import re
import math
import numpy as numpy
import scipy

#fileio
fileName = 'B-large'
# fileName = 'test copy'
iFile = open(fileName + '.in', 'r')
oFile = open(fileName + ".out", 'w')
true = True
false = False

def getTime(C,F,X,R,n):
    time = 0
    for i in range(n):
        time += C/(R+i*F)
    # print time
    time += X/(R+n*F)
    return time

def func(C,F,X):
    R = 2.0
    # T = 
    #   C(1/R + 1/(R+F) + 1/(R+2F)) +...+ 1/(R+(n-1)F)
    # + X/(R+nF)
    
    vn = 1
    # Narrow down Valley
    # print 'narrow1'
    while true:
        time = getTime(C,F,X,R,vn)
        lastTime = getTime(C,F,X,R,vn-1)
        # print time, lastTime, vn
        if time >= lastTime:
            break
        vn += 1500


    # Narrow down Valley
    # print 'narrow2'
    vn -= 1500
    while true:
        time = getTime(C,F,X,R,vn)
        lastTime = getTime(C,F,X,R,vn-1)
        # print time, lastTime, vn
        if time >= lastTime:
            break
        vn += 50

    # Real run
    # print 'real', vn
    minTime = X/R # No farm
    lastTime = X/R
    for n in range(max(vn-50, 1), vn+1):
        time = getTime(C,F,X,R,n)
        minTime = min(minTime, time)
        # print time, lastTime, n
        if time >= lastTime:
            break
        lastTime = time
        n += 1
    # print minTime
    return "{0:.7f}".format(minTime)

#main
inputNum = int(iFile.readline())
count = 0
lines = iFile.readlines()
###


###
for i in range(inputNum):
    result = ''
    arr = [0]*100
    ###
    # CFX
    line = lines[i]
    C,F,X = eval(line.replace(' ', ', '))
    
    
    ###
    result = func(C,F,X)
    ###
    
    
    ###
    #normal
    count += 1
    resultStr = "Case #"+str(count)+": "+str(result)
    print resultStr
    oFile.write(resultStr+'\n')

#fileio
iFile.close()
oFile.close()


