t=input()
for case in range(1,t+1):
    n=input()
    m=map(int,raw_input().split())
    y=0
    z=0
    ckk=0
    for i in range(1,n):
        if m[i]-m[i-1]<0:
            y+=(m[i-1]-m[i])
        ckk=max(ckk,m[i-1]-m[i])
    for i in range(n-1):
        if m[i]>=ckk:z+=ckk
        else:z+=m[i]
    print "Case #"+`case`+": "+`y`+" "+`z`
