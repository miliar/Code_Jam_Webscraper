#!/usr/bin/env python
#encoding=utf-8

'''
author:     Eric Zhang(snow31450588@gmail.com)
purpose:    Google Code Jam Qualification Round
history:
    2014-04-11  Initial version
'''

import sys
import string
def getTimeNoFarm(X, production):
    return X/production

def getTimeFarm(X, C, F, production):
    return C/production + X/(production+F)
    
def calc(C,F,X):
    print C,F,X
    time = 0.0
    production = 2.0
    timeNoFarm = getTimeNoFarm(X, production)
    timeFarm = getTimeFarm(X, C, F, production)
    while timeNoFarm > timeFarm:
        time += C/production
        production += F
        #print C,F,X,time,production, timeNoFarm, timeFarm
        timeNoFarm = getTimeNoFarm(X, production)
        timeFarm = getTimeFarm(X, C, F, production)
    time += timeNoFarm
    return time

def wf(fileName,results):
    f = open(fileName,'w')
    for i,r in enumerate(results):
        f.write('Case #%d: %f\n'%(i+1,r))
    f.close()

def rf(fileName):
    f = open(fileName,'r')
    inputs = []
    n = int(f.readline())
    for i in range(n):
        ls = f.readline().strip().split()
        inputs.append([float(l) for l in ls])
    return inputs

def main(fin, fout):
    results = []
    
    for C,F,X in rf(fin):
        e = calc(C,F,X)
        results.append(e)
    
    wf(fout,results)


if __name__=='__main__':
    fin = sys.argv[1]
    fout = sys.argv[1][:-2]+'out'
    main(fin, fout)
    