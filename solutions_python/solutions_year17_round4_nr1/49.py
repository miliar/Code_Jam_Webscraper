from pprint import pprint

for nb in range(int(input())):
    #²n=int(input())
    n,p=[int(i) for i in input().split()]
    l=[int(i) for i in input().split()]
    #data=[[int(i) for i in input().split()] for p in range(r)]
    m = list(l)
    m =[e%p for e in m]
    x=[0]*p
    for e in m:
        x[e]+=1
    #pprint(x)
    """
    s=x[0]+1
    x[0]-=x[0]
    for i in range(1,(p)//2):
        e+=min(x[i],x[p-i])
        s+=e
        x[i+1]-=e
        x[n-i]-=e
    pprint(x)

    print(s)
    for i in range(p):

        if x[i]:
            print('i',i)
            for j in range(p):
                if x[j]:
                    print('j',j)
                    for k in range(p):
                        if x[k]:
                            print('k',k)
                            if (i+j+k)%p==0:
                                t=[0]*p
                                t[i]+=1
                                t[j]+=1
                                t[k]+=1
                                e=min(x[v]//t[v] for v in range(p) if t[v])
                                print('e',e)
                                s+=e
                                x[i]-=e
                                x[j]-=e
                                x[k]-=e
    pprint(x)
    print(s)
    """

    s=[0]
    def all_tupple(l,v):
        #print('v',v)
        if l==0:
            if sum(v)%p==0:
                t=[0]*p
                for e in v:
                    t[e]+=1
                e=min(x[i]//t[i] for i in range(p) if t[i])
                s[0]+=e
                for i in v:
                    x[i]-=e
        else:
            for i in range(p):
                all_tupple(l-1,v+[i])

    for l in range(1,p+1):
        all_tupple(l,[])
    #print(s)
    #pprint(x)
    if sum(x)==0:
        s=s[0]
    else:
        s=s[0]+1
    print("Case #"+str(nb+1)+":",s)
