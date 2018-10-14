import time
##import sys
##sys.setrecursionlimit(10002)
INFILE='bs.in'
OUTFILE='b.out'

from collections import defaultdict
def solve(n,c,m,mx):
    d=[defaultdict(int) for i in range(c+1)]
    for a,b in mx:
        d[b][a]+=1
    ans0=max([sum(di.values()) for di in d[1:]])
    ans1=0
    for i in d[1]:
        if d[1][i]+d[2][i]>ans0:
            if i==1:
                ans0=d[1][i]+d[2][i]
                ans1=0
            else:
                ans1=d[1][i]+d[2][i]-ans0
            break
    return '%d %d'%(ans0,ans1)



def read_input(fi):
    read=lambda type:type(fi.readline()[:-1])
    readArray=lambda type:map(type,fi.readline().split())
    readMatrix=lambda type,x:[map(type,fi.readline().split()) for i in range(x)]
    readLines=lambda type,x:[type(fi.readline()[:-1]) for i in range(x)]
    n,c,m=readArray(int)
    mx=readMatrix(int,m)
    return n,c,m,mx

def main():
    fi=file(INFILE)
    fo=file(OUTFILE,'w')
    time0=time.time()
    t=int(fi.readline())
    for ti in range(t):
        time1=time.time()
        t=read_input(fi)
        ans="Case #%d: %s"%(ti+1,solve(*t))
        print ans,"%.3f"%(time.time()-time1)
        fo.write(ans+'\n')
    print "%.3f"%(time.time()-time0)
    fi.close()
    fo.close()


if __name__ == '__main__':
    main()
    from random import randint