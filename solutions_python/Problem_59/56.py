'''
Created on 2010/05/23

@author: banana
'''

import math

import string



if __name__ == '__main__':
    pass


fp = open("A-large.in", "r")

line = fp.readline()

T = int(line)

fpout = open("2A-large.txt", "w")

for t in xrange(1, T+1):
    line = fp.readline()
    N = int(line.split()[0])
    M = int(line.split()[1])
    
    base = []
    for i in range(N):
        base.append(fp.readline().rstrip())

    target = []
    for i in range(M):
        target.append(fp.readline().rstrip())
    
    dirs = {}
    
    count = 0
    for path in base:
        path1 = path.split("/")
        path1 = path1[1:len(path1)]
        
        curdir = dirs
        for s in path1:
            if not curdir.has_key(s):
                curdir[s] = {}
                count = count + 1
            curdir = curdir[s]
    
    count = 0
    for path in target:
        path1 = path.split("/")
        path1 = path1[1:len(path1)]
        
        curdir = dirs
        for s in path1:
            if not curdir.has_key(s):
                curdir[s] = {}
                count = count + 1
            curdir = curdir[s]
        
    fpout.write("Case #%d: %d\n"%(t, count))
    print "Case #%d: %d"%(t, count)
     