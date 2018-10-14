fin=open('C-small-attempt0.in','r')
fo=open('C-small.out','w')
t=int(fin.readline())
i=0
while i<t:
    i+=1
    s=fin.readline()
    r,k,n=map(int,s.split())
    group=map(int,fin.readline().split())
    run=0
    pos=0
    income=0
    
    while run<r:
        run+=1
        onride=0
        onridec=0
        while onride<=k and onridec<=n:
            x=group[pos]
            onride+=x
            onridec+=1
            pos=(pos+1)%n
        onridec-=1
        onride-=x
        pos=(pos-1)%n
        income+=onride
    fo.write('Case #%d: %d\n'%(i,income))
fo.close()
fin.close()
