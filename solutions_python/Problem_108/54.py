T=int(input())
for t in range(T):
    N = int(input())
    ds,ls = [],[]
    for i in range(N):
        di,li = [int(x) for x in input().split()]
        ds.append(di)
        ls.append(li)
    D = int(input())
    best = [0]*N
    j = 0
    best[0] = ds[0]
    for i in range(N):
        while j<N and ds[i]+best[i]>=ds[j]:
            if best[j]==0:
                best[j] = min(ls[j],ds[j]-ds[i])
            j+=1
    if max([b+ds[i] for i,b in enumerate(best) if b>0])>=D>0:
        ans = "YES"
    else:
        ans = "NO"

    print('Case #',t+1,': ',ans,sep = '')
