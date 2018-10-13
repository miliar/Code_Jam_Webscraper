import sys
import fileinput
import re
import math
import numpy as numpy
import scipy

#fileio
### remember to change!!! ###
fileName = 'D-large'
# fileName = 'test'
iFile = open(fileName + '.in', 'r')
oFile = open(fileName + ".out", 'w')
true = True
false = False

def war(n, k):
    r = 0
    nk = k[:]
    for i in range(len(n)):
        nWin = true
        for x in nk:
            if n[i] < x:
                nWin = false
                nk.remove(x)
                break
        if nWin:
            r += 1
            nk.remove(nk[0])
    return r

# lose - force Ken to use the best card
# win - higher then all cards Ken has, force him to use the worst card
def dwar(n, k):
    r = 0
    nk = k[:]
    for i in range(len(n)):
        if n[i] < nk[0]:
            nk.remove(nk[len(nk)-1]) #lose
        else:
            nk.remove(nk[0]) # win
            r += 1
    return r

def main():
    inputNum = int(iFile.readline())
    count = 0
    lines = iFile.readlines()
    ###
    ###
    for i in range(inputNum):
        result = ''
        arr = [0]*100
        ###
        R = int(lines[i*3])

        naomi = sorted(map(float, lines[i*3+1].split(' ')))
        ken = sorted(map(float, lines[i*3+2].split(' ')))
        
        ###
        resultWar = war(naomi, ken)
        resultDWar = dwar(naomi, ken)
        ###
        
        
        ###
        #normal
        count += 1
        resultStr = "Case #"+str(count)+": "+str(resultDWar)+" "+str(resultWar)
        print resultStr
        oFile.write(resultStr+'\n')

    #fileio
    iFile.close()
    oFile.close()

main()