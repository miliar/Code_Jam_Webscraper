#!/usr/bin/env python
import sys

def mkdirs(cd, dirDict):
    lastIdx = cd.find('/')
    while lastIdx >= 0:
        lastIdx = cd.find('/', lastIdx+1)
        if lastIdx < 0:
            dirDict[cd] = ''
            break
        if cd[:lastIdx] not in dirDict:
            dirDict[cd[:lastIdx]] = ''

t = sys.stdin.readline().replace('\n','')

for x in range(int(t)):
    n,m = sys.stdin.readline().replace('\n','').split(' ')
    dirDict=dict()
    tot_mkdir = 0
    for y in range(int(n)):
        cd = sys.stdin.readline().replace('\n','')
        #print 'n: '+ cd
        mkdirs(cd, dirDict)
    tot_mkdir = -(len(dirDict))
    for z in range(int(m)):
        cd = sys.stdin.readline().replace('\n','')
        #print 'm: '+ cd
        mkdirs(cd, dirDict)
    #print dirDict
    tot_mkdir += len(dirDict)
    print "Case #%d: %d" % (x+1, tot_mkdir)
