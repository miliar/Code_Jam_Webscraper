fi=open("B-small-attempt0.in",'r')
fo=open("B-small-attempt0.out",'w')

t=int(fi.readline().strip())
for case in range(t):
    line=fi.readline().strip().split()
    l=int(line[0])
    t=int(line[1])
    n=int(line[2])
    c=int(line[3])
    
    do=[]
    d=[]
    ti=[0]
    
    for i in range(c):
        do.append(int(line[4+i]))
    while len(d)<n:
        for elem in do:
            d.append(elem)
        if len(d)==n:
            break
    
    for i in range(1,n+1):
        ti.append(ti[i-1]+d[i-1]*2)
    
    delta=[]
   
    for i in range(1,n+1):
        delta.append(ti[i]-max(ti[i-1],t))
    for i in range (l):
        ma=max(delta)
        delta.remove(ma)
        ti[n]-=ma/2
    fo.write("Case #"+str(case+1)+": "+str(ti[n])+"\n")
    
fi.close()
fo.close()