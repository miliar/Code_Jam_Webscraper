import time
##import sys
##sys.setrecursionlimit(10002)
INFILE='al.in'
OUTFILE='a.out'


def solve(r,c,mx):
    ans=[list(i) for i in mx]
    bi=-1
    for i in range(r):
        if ans[i]==['?']*c and (i==0 or ans[i-1][0]=='?'):
            bi=i
            continue
        if ans[i]==['?']*c:
            for j in range(c):
                ans[i][j]=ans[i-1][j]
            continue
        bj = -1
        for j in range(c):
            # print ans[i],j,ans[i][j]=='?',(j==0 or ans[i][j-1]=='?')
            if ans[i][j]=='?' and (j==0 or ans[i][j-1]=='?'):
                bj=j;print 'bj=',bj
                continue
            if ans[i][j]=='?':
                ans[i][j]=ans[i][j-1]
        # print bj
        for k in range(bj,-1,-1):
            # print i,k,ans[i]
            ans[i][k]=ans[i][k+1]
    for i in  range(bi,-1,-1):
        for j in range(c):
            ans[i][j]=ans[i+1][j]
    ans='\n'+'\n'.join([''.join(i) for i in ans])

    return ans



def read_input(fi):
    read=lambda type:type(fi.readline()[:-1])
    readArray=lambda type:map(type,fi.readline().split())
    readMatrix=lambda type,x:[map(type,fi.readline().split()) for i in range(x)]
    readLines=lambda type,x:[type(fi.readline()[:-1]) for i in range(x)]
    r,c=readArray(int)
    mx=readLines(str,r)
    return r,c,mx

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
