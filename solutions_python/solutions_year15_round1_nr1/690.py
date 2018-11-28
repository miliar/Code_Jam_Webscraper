case=int(input())
z=1
while z<=case:
    n=int(input())
    m=input().split()
    s1=0
    s2=0
    for i in range(n):
        m[i]=int(m[i])
    r1=0
    r2=0
    for i in range(0,n-1):
        if (m[i]-m[i+1])>r2:
            r2=m[i]-m[i+1]
    for i in range(0,n-1):
        if m[i]>m[i+1]:   
            r1=m[i]-m[i+1]
        elif m[i]==m[i+1]:
            r1=0
        else:
            r1=0
        if r1<m[i]:
            s1+=r1
        else:
            s1+=m[i]
        if r2<m[i]:
            s2+=r2
        else:
            s2+=m[i]
    print("Case #"+str(z)+":",s1,s2)
    z+=1
            
