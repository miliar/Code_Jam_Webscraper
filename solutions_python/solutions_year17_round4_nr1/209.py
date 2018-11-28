import time
##import sys
##sys.setrecursionlimit(10002)
INFILE='as.in'
OUTFILE='a.out'


def solve(n,p,nx):
    mx=[0]*p
    for i in nx:
        mx[i%p]+=1
    ans=mx[0]
    if p==2:
        ans+=mx[1]/2+mx[1]%2
    elif p==3:
        ans+=min(mx[1],mx[2])
        t=abs(mx[1]-mx[2])
        ans+=t/3+(1 if t%3 else 0)
    else:
        ans+=mx[2]/2
        ans+=min(mx[1],mx[3])
        t=abs(mx[1]-mx[3])
        if mx[2]%2 and t>=2:
            ans+=1
            t-=2
        ans+=t/4+(1 if t%4 else 0)


    return ans



def read_input(fi):
    read=lambda type:type(fi.readline()[:-1])
    readArray=lambda type:map(type,fi.readline().split())
    readMatrix=lambda type,x:[map(type,fi.readline().split()) for i in range(x)]
    readLines=lambda type,x:[type(fi.readline()[:-1]) for i in range(x)]
    n,p=readArray(int)
    nx=readArray(int)
    return n,p,nx

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