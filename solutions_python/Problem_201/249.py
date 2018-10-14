def divide(m):
    if m==1:
        return [0,0]
    s=m/2
    a=[]
    if m%2==0:
        a.append(s)
        a.append(s-1)
    else:
        a.append(s)
        a.append(s)
    return a

for t in range(input()):
    dic={}
    n,k=map(int,raw_input().split())

    if n==k:
        print "Case #"+str(t+1)+": 0 0"
        continue
    dic[n]=1
    while k>0:
        m=max(dic.keys())
        i=dic[m]
        del dic[m]
        a=divide(m)
        if a[0] in dic:
            dic[a[0]]+=i
        else:
            dic[a[0]]=i
            
        if a[1] in dic:
            dic[a[1]]+=i
        else:
            dic[a[1]]=i
        k-=i

    print "Case #"+str(t+1)+":",
    print a[0],a[1]
        
