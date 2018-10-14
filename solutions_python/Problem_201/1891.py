import math
t=int(input())
f=open('/home/shubham/python_scripts/outputQ3shortNews.txt',"w")
for q in range(t):
    n,k=[int(i) for i in input().split(' ')]
    if(n==k):
        f.write("Case #%d: %d %d\n" % (q + 1,0,0))
        continue
    washrooms=[0]*(n+2)
    washrooms[0]=1
    washrooms[n+1]=1
    Rs=0
    Ls=0
    p=0
    for i in range(k):
        x=washrooms.index(1)
        MaxDist=-1
        MinDist=-1
        flag=0
        p = -1
        while (x < len(washrooms) - 1):
            y=washrooms[x+1:].index(1) + x +1
            while((y-x)//2 == 0):
                x=y
                if(x<len(washrooms) - 1):
                    y = washrooms[x+1:].index(1)+x+1
                else:
                    flag=1
                    break
            if(flag==1):
                break
            m = x+(y-x)//2
            Ls = washrooms[x+1 : m].count(0)
            Rs = washrooms[m+1 : y].count(0)
            #print("ls=%d rs=%d\n"%(Ls,Rs))
            if(min(Rs,Ls)==MinDist):
                if(max(Rs,Ls)>MaxDist):
                    MaxDist=max(Rs,Ls)
                    p=m
            elif(min(Rs,Ls)>MinDist):
                MinDist=min(Rs,Ls)
                MaxDist=max(Rs,Ls)
                p=m
            x=y
            #print(x,y)
        #print("p=",p)
        washrooms[p]=1
    #print(p)
    """print(washrooms)
    print(washrooms[935:947])"""
    left=washrooms[0:p]
    #print(left)
    left.reverse()
    Ls=left.index(1)
    Rs=washrooms[p+1:].index(1)
    #print(washrooms.count(0))
    f.write("Case #%d: %d %d\n" % (q + 1, max(Ls, Rs), min(Ls, Rs)))


