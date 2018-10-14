T=int(input())
for ind1 in range(T):
    vacant={}
    n,k=map(int,input().split())
    vacant[n]=1
    ind2=2

    while(ind2<=k):
        next_vacant={}
        for key,value in vacant.items():
            sub1=key//2
            sub2=(key-1)//2
            if sub1 in next_vacant:
                next_vacant[sub1]+=value
            else:
                next_vacant[sub1]=value
            if sub2 in next_vacant:
                next_vacant[sub2]+=value
            else:
                next_vacant[sub2]=value
        vacant=next_vacant
        ind2*=2
    # print(ind2)
    ind2//=2
    rem=k-ind2
    temp=list(sorted(vacant))
    temp.reverse()
    res=0
    # print(rem)
    for key in temp:
        if rem<vacant[key]:
            res=key
            break;  
        rem-=vacant[key]
    # print(vacant)
    # print(res)
    if res:
        print("Case #"+str(ind1+1)+": "+str(res//2)+" "+str((res-1)//2))
    else:
        print("Case #"+str(ind1+1)+": 0 0")