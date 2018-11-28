def inv(a):
    def mergesort(l):
        if len(l) <= 1: return (l,0)
        print(l)
        a,ai = mergesort(l[:len(l)//2]); b,bi = mergesort(l[len(l)//2:])
        ax,bx = 0,0
        tot = ai+bi
        newl = []
        for i in range(len(l)):
            if len(a) == ax:
                newl.append(b[bx]); bx += 1
            elif len(a) == bx:
                newl.append(a[ax]); ax += 1
            else:
                if a[ax] < b[bx]:
                    newl.append(a[ax]); ax += 1
                else:
                    newl.append(b[bx]); bx += 1
                    print("inc")
                    tot += len(a)-ax
        return (newl,tot)

    return mergesort(a)[1]

def solve(testnum):
    n = int(input())
    a = [int(x) for x in input().split()]
    assert len(a) == n
    a2 = sorted(a)
##    mx = max(a)
##    mi = a.index(mx)
##    l = a[0:mi]+a[mi+1:]
##    tot = n*(n+1)//2
##    for i in range(n):
##        cur = inv(l[:i])+inv(list(reversed(l[i:])))+abs(i-mi)
##        print(i,cur)
##        tot = min(cur,tot)
    #ans = inv(a[0:mi])+inv(a[-1:mi:-1])
    i,i2 = 0,n-1
    tot = 0
    for e in a2:
        i = a.index(e)
        tot += min(i,len(a)-i-1)
        a.remove(e)
    print("Case #%d: %d"%(testnum,tot))
        

for i in range(int(input())): solve(i+1)
