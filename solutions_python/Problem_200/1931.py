T=int(input())
for t in range(1,T+1):
    n=raw_input()
    a=list(n)
    b=[]
    for i in a:
        b.append(int(i))
    if(len(b)==1):
        print "Case #{}: {}".format(t, n)
        continue
    while(1):
        c=[]
        i=1
        flag1=0
        for i in range(1,len(b)):
            if(b[i]>=b[i-1]):
                c.append((b[i-1]))
            else:
                c.append((b[i-1]-1))
                flag1=1
                break
        if(flag1==1):
            for j in range(i,len(b)):
                c.append((9))
        else:
            c.append(b[i])
        flag=1
        for i in range(1,len(c)):
            if(c[i]<c[i-1]):
                flag=0
        if(flag==1):
            break
        b=c
    for i in range(len(c)):
        if(c[i]!=0):
            break
    ans=""
    for j in range(i,len(c)):
        ans+=str(c[j])
    print "Case #{}: {}".format(t, ans)
