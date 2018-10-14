import sys
import fileinput
import re
import math
import numpy as numpy
import scipy

#fileio ### remember to change!!! ###
# fileName = 'test' 
fileName = 'A-small-attempt0' 
iFile = open(fileName + '.in', 'r')
oFile = open(fileName + ".out", 'w')
true = True
false = False

def func(strr):
    r = ''
    answer1 = strr[0]
    answer2 = strr[5]
    line1 = strr[int(answer1)].replace('\n', '').split(' ')
    line2 = strr[5+int(answer2)].replace('\n', '').split(' ')
    print line1, line2
    common = set(line1)&set(line2)
    # print common
    if len(common) == 0:
        r = 'Volunteer cheated!'
    elif len(common) > 1:
        r = 'Bad magician!'
    else:
        r = list(set(common))[0]
    print r
    return r

#main
inputNum = int(iFile.readline())
count = 0
lines = iFile.readlines()
###
for i in range(inputNum):
    result = ''
    arr = [0]*100
    ###
    result = func(lines[i*10:i*10+10])    
    ###
    #normal
    count += 1
    resultStr = "Case #"+str(count)+": "+str(result)
    print resultStr
    oFile.write(resultStr+'\n')

#fileio
iFile.close()
oFile.close()


