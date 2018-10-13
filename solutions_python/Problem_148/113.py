##import sys
##sys.setrecursionlimit(10002)

def solve(n,x,m):
    m.sort()
    i=0;j=n-1
    ans=0
    while i<j:
        if m[i]+m[j]<=x:
            ans+=1
            i+=1;j-=1
        else:
            ans+=1
            j-=1
    if i==j:
        ans+=1
    return str(ans)

def main():
    fi=file('al.in')
    fo=file('a.out','w')
    t=int(fi.readline())
    for ti in range(t):
        n,x=map(int,fi.readline().split())
        m=map(int,fi.readline().split())
        ans="Case #%d: %s"%(ti+1,solve(n,x,m))
        print ans
        fo.write(ans+'\n')
    fi.close()
    fo.close()

if __name__ == '__main__':
    main()
