import sys
sys.setrecursionlimit(10002)

def solve(n,m):
    if n==1:
        return 0
    i=m.index(min(m))
    res=min(i,n-i-1)+solve(n-1,m[:i]+m[i+1:])
    return res

def main():
    fi=file('bl.in')
    fo=file('b.out','w')
    t=int(fi.readline())
    for ti in range(t):
        n=int(fi.readline())
        m=map(int,fi.readline().split())
        ans="Case #%d: %s"%(ti+1,solve(n,m))
        print ans
        fo.write(ans+'\n')
    fi.close()
    fo.close()

if __name__ == '__main__':
    main()
    #print solve(8,[2736815, 533043, 4714958, 413916, 8672317, 6310392, 2648052, 8580528])
