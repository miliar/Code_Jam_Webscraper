import time
import sys
sys.setrecursionlimit(10002)
INFILE='ds.in'
OUTFILE='d.out'

def check(row,c):
    return [i for i in row if i<>'.' and i<>c]==[]

def solve(n,m,mx):
    d={}
    ans={}
    ra=range(n)
    ca=range(n)
    dma=set(range(-n+1,n))
    dpa=range(0,n*2-1)
    for mi,r,c in mx:
        r-=1
        c-=1
        d[(r,c)]=mi
        if mi in ['o','x']:
            ra.remove(r)
            ca.remove(c)
        if mi in ['o','+']:
            dma.remove(r-c)
            dpa.remove(r+c)
    for i in range(len(ra)):
        if (ra[i],ca[i]) in d:
            d[(ra[i],ca[i])]='o'
            ans[(ra[i],ca[i])]='o'
        else:
            d[(ra[i],ca[i])]='x'
            ans[(ra[i],ca[i])]='x'
##    print d
    dpa.sort(key=lambda x:-abs(x-n))
    for i in range(len(dpa)):
        for r in range(n):
            c=dpa[i]-r
            if 0<=c<n and r-c in dma:
                if (r,c) in d:
                    d[(r,c)]='o'
                    ans[(r,c)]='o'
                else:
                    d[(r,c)]='+'
                    ans[(r,c)]='+'
                dma.remove(r-c)
                break
##    print d
##    for i in range(n):
##        for j in range(n):
##            print d.get((i,j),0),
##        print
    pts=sum([(2 if i=='o' else 1) for i in d.values()])
    res=["%d %d"%(pts,len(ans))]
    ans=["%s %d %d"%(v,k[0]+1,k[1]+1) for k,v in sorted(ans.items())]
    return '\n'.join(res+ans)


def read_input(fi):
    read=lambda type:type(fi.readline()[:-1])
    readArray=lambda type:map(type,fi.readline().split())
    readMatrix=lambda type,x:[map(type,fi.readline().split()) for i in range(x)]
    readLines=lambda type,x:[type(fi.readline()[:-1]) for i in range(x)]
    n,m=readArray(int)
    mx=readMatrix(str,m)
    mx=[(i[0],int(i[1]),int(i[2])) for i in mx]
    return n,m,mx

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
##    g=[['.', 'x', '.'], ['+', '+', '+'], ['x', '.', '.']]
##    r=0;c=1;n=3
