import sys
f3=open(sys.argv[1])
f3=f3.readlines()[1:]
i=0
for now in f3:
    i+=1
    print "Case #"+str(i)+":",
    now=now.split()
    n,s,p=(map(int,now[0:3]))
    all=map(int,now[3:])
    lp=p-2
    if lp<0:lp=0
    low=lp*2+p
    lp=p-1
    if lp<0:lp=0
    up=lp*2+p
    ans=0
    for j in all:
        if j>=up:
            ans+=1
        else:
            if s >0 and j>=low:
                s-=1
                ans+=1
    print ans
        
