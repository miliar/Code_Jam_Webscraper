import itertools 


def ud(a):
    lt = True
    for i in range(1,len(a)):
        if lt and a[i] > a[i-1]: continue
        lt = False
        if a[i]>=a[i-1]:return False
    return True
def sol():
    n = int(input())
    a = list(map(int,input().split()))
    ans = n*n*n
    for p in filter(ud,itertools.permutations(a)):
        b=[p.index(t) for t in a]
        tmp = 0
        for i in range(n):
            for j in range(i):
                if b[i]>b[j]:
                    tmp+=1
                if tmp >= ans:
                    break
        ans=min(ans,tmp)
    return ans

for i in range(int(input())):
    print( "Case #%d: %d"%(i+1,sol()))
