'''
Created on Apr 11, 2015

@author: Pango
'''

from os.path import basename
import re
import os

DEBUGMODE=True

### Functions ###
def debug(text):
    global DEBUGMODE
    if DEBUGMODE:
        print 'DEBUG:', text

def solveOne(row):
    ss = row.split(' ')
    sMax = int(ss[0])
    numList = ss[1]
    debug('input : ' + numList)
    
    invite = 0
    mySum = 0
    for i in range(sMax+1):
        n_i = int(numList[i])
        if i > mySum:
            invite_i = i - mySum
            debug('Need to invite %d for Level S_%d' % (invite_i, i))
            mySum += invite_i
            invite += invite_i
        mySum += n_i
    return invite

### Main ###
if __name__ == '__main__':
    inputFilepath = re.sub('\.py$', '', basename(__file__))+'.in'
    outputFilepath = re.sub('\.\w+$', '', inputFilepath)+'.out'

    with open(inputFilepath) as fp:
        with open(outputFilepath, 'w') as fpw:
            ln = fp.readline().rstrip()
            caseNumber = int(ln)
            for i in range(caseNumber):
                ln = fp.readline().rstrip()
                answer = 'Case #%d: %d' % ((i+1), solveOne(ln))
                print answer
                fpw.write(answer + os.linesep)
