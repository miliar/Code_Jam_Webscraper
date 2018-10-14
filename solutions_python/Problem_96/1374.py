t=input()
for i in range(t) :
    inp=map(int,raw_input().split())
    n,s,p=inp[:3]
    cnt=0
    for x in inp[3:] :
        a=x/3
        b=x-a*3
        if a>=p or (a==p-1 and b>0) :
            cnt+=1
        elif (a==p-1 and a>0) or (a==p-2 and b==2) :
            if s>0:
                cnt+=1
                s-=1
    print "Case #%d:"%(i+1),cnt


