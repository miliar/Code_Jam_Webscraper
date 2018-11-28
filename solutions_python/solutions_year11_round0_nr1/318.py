#!/bin/python
#import sys
#sys.stdin = file("sample.in")

def readint(): return int(raw_input())

def readints(): return [ int(x) for x in raw_input().split() ]

def index(name):
    if name == 'O':
        return 0
    return 1

def rev(index):
    if index == 0:
        return 1
    return 0

def solve(alist):
    ret = 0
    pos = [1,1]
    time = [0,0]
    for act in alist:
        i = index(act[0])
        r = rev(i)
        b = act[1]
        
        needtime = abs(b - pos[i]) + 1
        if time[i] - needtime >= 0:
            needtime = 1
        else:
            needtime = needtime - time[i]

        pos[i] = b
        time[i] = 0
        time[r] += needtime
        ret += needtime
    return ret

if __name__ == "__main__":
    nt = readint()
    for i in range(nt):
        line = raw_input().split()
        ne = int(line[0])
        alist = zip(line[1::2],[ int(x) for x in line[2::2]])
        print "Case #%d: %d" % ( i+1, solve(alist))
