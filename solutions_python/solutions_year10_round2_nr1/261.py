'''
Created on May 21, 2010

@author: trmcjilt
'''
import sys
from math import sqrt,ceil,floor
filename="A-large.in"
#filename="sample.in"
file = open(filename,'r')
sys.stdout = open(filename+".out",'w')


numOfCases = int(file.readline().strip())
caseNum = 1
def addDirToMap(map,directories):
    i = 0
    tempMap=map
    for dir in directories:
        if not tempMap.has_key(dir):
            tempMap[dir] = {}
            i+=1
        tempMap = tempMap[dir]
    return i
while numOfCases >= caseNum:
    N,M = map(int,file.readline().strip().split(' '))
    dmap = {}
    value = 0
    i = 0
    while i < N:
        directories = file.readline().strip().split('/')[1:]
        addDirToMap(dmap,directories)
        i+=1
    i=0
    while i < M:
        directories = file.readline().strip().split('/')[1:]
        value += addDirToMap(dmap,directories)
        i+=1
        
    print "Case #%(caseNum)s: %(value)s"%locals()
    caseNum+=1
    
    
    
    
    