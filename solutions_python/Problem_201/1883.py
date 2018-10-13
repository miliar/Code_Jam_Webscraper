#!/usr/bin/env python
#coding:utf-8
#---------------------------------------------------------------------
import sys
import os
#---------------------------------------------------------------------
def getSolve(N, K):
    N = int(N)
    K = int(K)
    if N <= K:
        return 0,0
    mx = N
    mn = N
    XXX = [N]
    ml = 0
    mr = 0
    for i in range(0, K):
        mx = [0,0]
        for j, b in enumerate(XXX):
#            print j, b
            if mx[0] < b:
               mx[0] = b 
               mx[1] = j
        #XXX = XXX[:mx[1]] + [int(mx[0]/2) + mx[0] % 2, int(mx[0]/2) - 1] + XXX[mx[1]+1:]
        ml = int(mx[0]/2) 
        mr = int(mx[0]/2) + mx[0] % 2 - 1
        XXX = XXX[:mx[1]] + [ml, mr] + XXX[mx[1]+1:]
        #print XXX
        #mn = int(mx/2) - 1 + mx % 2
        #mx = int(mx/2)
        #print i,mx,mn
    #return max(XXX), min(XXX)
    return ml, mr
#---------------------------------------------------------------------
def main():
    if len(sys.argv) == 2:
        if os.path.isfile(sys.argv[1]) is False:
            print "dose not found file", sys.argv[1]
            return
        i = 0
        with open(sys.argv[1], 'r') as f:
            buffs = f.readlines()
            for i, buff in enumerate(buffs):
                if i != 0:
                    buff = buff.strip()
                    b = buff.split(' ')
#                    print buff
                    x = getSolve(b[0], b[1])
                    print 'Case #%d: %d %d'% (i ,x[0], x[1])
                i += 1
#---------------------------------------------------------------------
if __name__ == '__main__':
    main()
#---------------------------------------------------------------------
