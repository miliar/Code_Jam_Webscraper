n=int(raw_input())
def solve(lis,inv,n,m):
    lis1=[[max(row)]*m for row in lis]
    inv1=map(list,zip(*lis1))
    for i,col in enumerate(inv1):
        if col!=inv[i]:
            minn=min(inv[i])
            inv1[i]=[minn if x>minn else x for x in inv1[i]]
            if inv1[i]!=inv[i]:
                return "NO"
    else:
        return "YES"            
for case in xrange(n):
    n,m=map(int,raw_input().split())
    lis=[map(int,raw_input().split()) for i in xrange(n)]
    inv=map(list,zip(*lis))
    print "Case #{0}: {1}".format(case+1,solve(lis,inv,n,m))
