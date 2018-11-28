DEBUG=0
PARALELL=0
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
def f1(s):
        cc=None
        cct=0
        s=[x for x in s]
        s+=[1]
        out=[]
        for c in s:
            if c!=cc:
                if cc:
                    out.append((cc, cct))
                cct=1
                cc=c
            else:
                cct+=1
        #print out
        return out
def solve(INPUT):
        N,M=INPUT
        MM=[]
        for m in M:
            MM.append(f1(m))
        m0=MM[0]
        for m in MM[1:]:
            if len(m)!=len(m0):
                return "Fegla Won"
            for i in range(len(m)):
                if m[i][0]!=m0[i][0]:
                    return "Fegla Won"
            
        answer=0
        for i in range(len(m0)):
            avg=m0[i][1]
            for m in MM[1:]:
                avg+=m[i][1]
            print 'sumavg',avg
            avg=int(round(1.0*avg/len(MM)))
            print 'avg',avg
            answer+=abs(m0[i][1]-avg)
            for m in MM[1:]:
                answer+=abs(m[i][1]-avg)
        return str(answer)
def readit(t):
        N=getInt()
        M=[]
        for i in range(N):
            M+=getStrings()
        
        return (N, M)

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
