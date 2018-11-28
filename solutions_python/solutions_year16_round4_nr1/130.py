import time
##import sys
##sys.setrecursionlimit(10002)
INFILE='al.in'
OUTFILE='a.out'


def solve(n,r,p,s):
    m=(2**n-2)/2
    if m%3==0:
        # a,b,c=m/3*2,m/3*2+1,m/3*2+1
        if r==p-1 and p==s:
            res='PRS'
        elif p==r-1 and r==s:
            res='SPR'
        elif s==p-1 and p==r:
            res='RSP'
        else:
            return 'IMPOSSIBLE'
        r1 = (''.join([i + i for i in res]))
        r2=list( res[2]+r1*(m/3)+res[0])
    else:
        if r==p+1 and p==s:
            res='PRS'
        elif p==r+1 and r==s:
            res='SPR'
        elif s==p+1 and p==r:
            res='RSP'
        else:
            return 'IMPOSSIBLE'
        r1=(''.join([i+i for i in res]))*(m/3+1)
        r2=list( r1[1:2**n+1])
    for i in range(1,n+1):
        for j in range(0,2**n,2**i):
            step=2**(i-1)
            if r2[j:j+step]>r2[j+step:j+step*2]:
                r2[j:j+step],r2[j+step:j+step*2]=r2[j+step:j+step*2],r2[j:j+step]
    return ''.join(r2)



def read_input(fi):
    read=lambda type:type(fi.readline()[:-1])
    readArray=lambda type:map(type,fi.readline().split())
    readMatrix=lambda type,x:[map(type,fi.readline().split()) for i in range(x)]
    readLines=lambda type,x:[type(fi.readline()[:-1]) for i in range(x)]
    n,r,p,s=readArray(int)
    return n,r,p,s

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
    # print solve(12,1365,1365,1366)
