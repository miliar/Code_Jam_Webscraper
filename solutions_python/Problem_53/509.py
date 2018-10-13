'''
Created on May 7, 2010

@author: trmcjilt
'''
import sys
filename="A-large.in"
#filename="file.txt"
file = open(filename,'r')
sys.stdout = open(filename+".out",'w')

numOfCases = int(file.readline().strip())
caseNum = 1
while numOfCases >= caseNum:
    state = 0
    case = map(int,file.readline().strip().split(' '))
    state = (case[1]+1)%(2**case[0]) == 0
    value = "ON" if state else "OFF"
    print "Case #%(caseNum)s: %(value)s"%locals()
    caseNum += 1
