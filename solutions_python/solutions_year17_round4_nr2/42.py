from pprint import pprint

for nb in range(int(input())):
    #n=int(input())
    n,c,m=[int(i) for i in input().split()]
    #l=[int(i) for i in input().split()]
    data=[[int(i) for i in input().split()] for _ in range(m)]

    l=[p for p,i in data]
    l.sort()
    #pprint(l)
    min_coster=max((-(-(i+1)//l[i]))for i in range(m))
    #print(min_coster)

    l=sorted(data,key=lambda x:x[::-1])
    #pprint(l)

    last=-1
    for p,i in l:
        if i!=last:
            t=0
            last=i
        t+=1
        min_coster=max(min_coster,t)
    #print(min_coster)

    l=[p for p,i in data]
    l.sort()
    #pprint(l)
    total=0
    rank=n
    free=min_coster
    for i in range(m):
        i=m-i-1
        if rank == l[i]:
            if free==0:
                rank-=1
                free=min_coster
                total+=1
            else:
                free-=1
        elif rank>l[i]:
            rank=l[i]
            free=min_coster-1
        elif rank<l[i]:
            if free==0:
                rank-=1
                free=min_coster
                total+=1
            else:
                total+=1
        #print(total)

    s=min_coster
    print("Case #"+str(nb+1)+":",s,total)
