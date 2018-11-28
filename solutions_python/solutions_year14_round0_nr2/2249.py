__author__ = 'Wei'

import math

def B():
    num = int(raw_input())
    for i in xrange(num):
        args = readints()
        time = cal(args[0],args[1],args[2])
        print "Case #" + str(i+1) + ":", str(time)

def readints():
    return [float(x) for x in raw_input().split(' ')]

def cal(C,F,X):
   k = max(int(math.floor(X/C - 2/F)),0)
   return find(C,F,X,k)

def find(C,F,X,k):
    t = 0
    for i in range(k):
        t += C/(2+i*F)
    t += X/(2+k*F)
    return t

B()