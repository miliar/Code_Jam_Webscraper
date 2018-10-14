def standingOvation(filename):
    f=open(filename,'rU')
    tc=int(f.readline())
    g=open('standingOvationLarge.out','w')

    for i in range(tc):
        line=f.readline()
        b=line.split()
        smax=int(b[0])
        a=b[1]
        p=0
        rp=0
        for j in range(smax+1):
            if j>p+rp:
                rp=j-p
            p+=int(a[j])
        g.write(('Case #%d: %d\n')%(i+1,rp))
    f.close()
    g.close()
standingOvation('A-large.in')
        
            
