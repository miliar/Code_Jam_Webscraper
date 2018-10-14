from sys import stdin
from math import *

T = int(stdin.readline())

def compare(d1,d2):
    d1l = d1.split('/')
    d2l = d2.split('/')
    
    if len(d1l) < len(d2l): return -1
    if len(d1l) == len(d2l): return 0
    if len(d1l) > len(d2l): return 1
     

for t in xrange(0, T):
    line = stdin.readline()
    nums = line.split()
    N = int(nums[0])
    M = int(nums[1])
    dirs = []
    dirs.append("/")
    for i in xrange(0,N):
        dir = stdin.readline()
        dir = dir.strip()
        if (dirs.count(dir)==0):
            dirs.append(dir)
        
    newdirs = []    
    for i in xrange(0,M):
        dir = stdin.readline()
        dir = dir.strip()
        if (newdirs.count(dir)==0):
            newdirs.append(dir)
    
    newdirs.sort(cmp=compare)
    
    count = 0
    for dir in newdirs:
        if (dirs.count(dir) ==0):
            dl = dir.split('/')
            dl.pop(0)
            path = '/'
            for subdir in dl:
                path = path + subdir
                if not path in dirs:
                    dirs.append(path)
                    count+=1
                path+="/"

    print "Case #" + str(t + 1) + ":",count
    
