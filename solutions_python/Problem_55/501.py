'''
Created on May 7, 2010

@author: trmcjilt
'''
import sys
filename="C-small-attempt0.in"
#filename="file.txt"
sys.stdout = open(filename+".out",'w')

file = open(filename,'r')
numOfCases = int(file.readline().strip())
caseNum = 1
while numOfCases >= caseNum:
    [Runs,CarSize] = map(int,file.readline().strip().split(' '))[0:2]
    GroupList = map(int,file.readline().strip().split(' '))
    total = 0
    for run in xrange(Runs):
        riders = 0
        tempQ = []
        while len(GroupList) and GroupList[0]+riders <= CarSize :
#            print "Before\tRun:%(run)s\tGroupList:%(GroupList)s"%locals()
            riders+=GroupList[0]
            tempQ.append(GroupList.pop(0))
#            print "After\tRun:%(run)s\tGroupList:%(GroupList)s"%locals()
#            print "Riders:",riders,"\tCarSize:",CarSize
        total+=riders 
        GroupList+=tempQ
    
    value=total
    print "Case #%(caseNum)s: %(value)s"%locals()
    caseNum += 1