DEBUG=0
PARALELL=1
TEST=0
SOLVE=1
################## TEMPLATE###################
import random
from pprint import pprint 
from collections import defaultdict
import heapq, struct

def prnt(x): 
    if DEBUG: 
        pprint(x)
if 'PyPy' not in copyright.__str__():
    PARALELL=0
if PARALELL:
    from multiprocessing import Process, cpu_count
    cpus=cpu_count()
    def poolmap(f,m, chunksize=None):return pool.map(f,m,chunksize)
else:
    cpus=1
    def poolmap(f,m, chunksize=None):return map(f,m)
def test():pass

################## TEMPLATE###################


def do(parent, root, DG):
    hijos=[]
    if len(filter(lambda x: x!=parent, DG[root]))<2:
        return 1
    
    for leaf in DG[root]:
        if leaf!=parent:
            hijos.append(do(root,leaf, DG))
    hijos.sort()
    r=sum(hijos[-2:])+1
    return r
from fractions import *
def solve(INPUT):
        size, fs=INPUT
        fs.sort()
        ct=0
        for j in range(len(fs)-1, 0-1, -1):
            mx=fs[j]
            if mx==0:
                continue
            candidate=None
            for i in range(j):
                f= fs[i]
                if f :
                    if f+mx<=size:
                        candidate=i
                    else:
                        break
            if candidate!=None:
                fs[candidate]=0
            ct+=1
            
        
        return str(ct)
def readit(t):
        n, size=getInts()
        fs=getInts()
        return (size, fs)

def run():
    T=getInt()
    INPUT=map(readit, range(T))
    answers=poolmap(solve,  INPUT)
    
    for t in range(T):
        outputFile.write( "Case #%d: %s\n"%(t+1,answers[t]))
    outputFile.close()
############# TEMPLATE ##########
 
import os
filename= os.path.basename(__file__)[:-3]
def getFloat():
    r=inputFile.readline()
    try:
        r= float(r)
        if DEBUG:
            print 'getFloat: ', r
        return r
    except:
        print 'Error parsing %r'%r
        raise
def getInt():
    r=inputFile.readline()
    try:
        r= int(r)
        if DEBUG:
            print 'getInt: ', r
        return r
    except:
        print 'Error parsing %r'%r
        raise
def getInts():
    return map(int,getStrings())
def getFloats():
    return float(int,getStrings())
def getStrings():
    r=inputFile.readline().split()
    if DEBUG:
        print 'getStrings: ', r
    return r

inputFile=file('%s.in'%filename, 'r')
outputFile=file('%s.out'%filename, 'w')

if __name__=='__main__':
    if PARALELL:
        from multiprocessing import Pool
        pool=Pool()
        
    if TEST:
        test()
    if SOLVE:
        run()
