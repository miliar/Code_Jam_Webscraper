import time
##import sys
##sys.setrecursionlimit(10002)
INFILE='al.in'
OUTFILE='a.out'
import bisect
from heapq import nlargest
from math import pi
def solve(n,k,nx):
    nx1=sorted(nx,reverse=1)
    nx2=sorted([(i[1]*i[0],i[0]) for i in nx])
    ans=0
    for i in range(n):
        if i>0 and nx1[i-1][0]==nx1[i][0]:
            continue
        nx2=[ni for ni in nx2 if ni[1]<=nx1[i][0]]#;print nx2,nx1[i][0]
        if len(nx2)<k:
            continue
        p=bisect.bisect_left(nx2,(nx1[i][1]*nx1[i][0],nx1[i][0]))
        if p>=len(nx2)-k:
            h=sum([ni[0] for ni in nx2][len(nx2)-k:])
        else:
            h=sum([ni[0] for ni in nx2][len(nx2)-k+1:])+nx1[i][1]*nx1[i][0]
        r=nx1[i][0]
        res=r*r+2*h
        ans=max(ans,res)
        # print nx1[i],res,ans,h,r,nx2,p
    return ans*pi

def read_input(fi):
    read=lambda type:type(fi.readline()[:-1])
    readArray=lambda type:map(type,fi.readline().split())
    readMatrix=lambda type,x:[map(type,fi.readline().split()) for i in range(x)]
    readLines=lambda type,x:[type(fi.readline()[:-1]) for i in range(x)]
    n,k=readArray(int)
    nx=readMatrix(int,n)
    return n,k,nx

def main():
    fi=file(INFILE)
    fo=file(OUTFILE,'w')
    time0=time.time()
    t=int(fi.readline())
    for ti in range(t):
        time1=time.time()
        ans="Case #%d: %s"%(ti+1,solve(*read_input(fi)))
        print ans,"%.3f"%(time.time()-time1)
        fo.write(ans+'\n')
    print "%.3f"%(time.time()-time0)
    fi.close()
    fo.close()

if __name__ == '__main__':
    main()
    # n=1000;k=500
    # nx=[]
    # from random import randint
    # for i in range(n):
    #     nx.append([randint(1,10000),randint(1,10000)])
    # print solve(n,k,nx)
