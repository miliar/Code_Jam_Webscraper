

n=int(input())

for nb in range(n):
    l,n=[int(i) for i in input().split()]
    d={l:1}
    i=0
    n=n-1
    #print(i,n,d)
    while n:
        v=max(v for v in d if d[v])
        e=d[v]
        if n>=e:
            n-=e
            del d[v]
            if v%2==1:#impair
                if v//2 not in d:
                    d[v//2]=0
                d[v//2]+=2*e
            else:#pair
                if v//2 not in d:
                    d[v//2]=0
                d[v//2]+=e
                if (v//2)-1 not in d:
                    d[(v//2)-1]=0
                d[(v//2)-1]+=e
        else:
            """
            if v%2:#impair
                d.append((v//2,2*n))
            else:#pair
                d.append((v//2,n))
                d.append(((v//2)-1,n))
            """
            n=0

    v=max(v for v in d if d[v])
    e=d[v]
    #print(v,e,d)
    print("Case #"+str(nb+1)+": "+str(v//2)+" "+str((v-1)//2))
    """while nb+1==20:
        pass"""
