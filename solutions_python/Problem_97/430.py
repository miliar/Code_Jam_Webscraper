import sys
f3=open(sys.argv[1])
f3=f3.readlines()[1:]
i=0
for now in f3:
    i+=1
    print "Case #"+str(i)+":",
    di=dict()
    a,b=map(int,now.split())
    for j in range(a,b+1):
        k=str(j)
        temp=k
        for kk in range(0,len(k)):
            temp=temp[-1:]+temp[:-1]
            if temp<k:
                k=temp

        if k in di:
            di[k]+=1
        else:
            di[k]=1
    ans=0
    for j in di:
        temp=di[j]
        ans+=temp*(temp-1)
    print ans/2
        
