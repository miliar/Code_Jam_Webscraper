f=open("B-large.in")
g=open("B.out","w")
T=int(f.readline())
for case in xrange(1,T+1):
    avex=0
    avey=0
    avez=0
    avevx=0
    avevy=0
    avevz=0
    N=int(f.readline())
    for i in xrange(N):
        ind=map(float,f.readline().split())
        avex+=ind[0]
        avey+=ind[1]
        avez+=ind[2]
        avevx+=ind[3]
        avevy+=ind[4]
        avevz+=ind[5]
    avex/=N
    avey/=N
    avez/=N
    avevx/=N
    avevy/=N
    avevz/=N
    if avevx!=0:
        m=avevz/avevx
        n=avevy/avevx
        c=avez-m*avex
        d=avey-n*avex
        xsol=(0-2*m*c-2*n*d)/(2*(m*m+n*n+1))
        dist=((xsol*xsol)*(m*m+n*n+1)+2*xsol*(m*c+n*d)+c*c+d*d)**0.5
        time=xsol-avex
        time/=avevx
        if time>=0:
            g.write("Case #"+str(case)+": "+str(dist)+" "+str(time)+"\n")
        else:
            g.write("Case #"+str(case)+": "+str((avex*avex+avey*avey+avez*avez)**0.5)+" 0\n")
    elif avevz!=0:
        m=avevy/avevz
        c=avey-m*avez
        zsol=(0-c*m)/(m*m+1)
        dist=((zsol*zsol)*(m*m+1)+2*zsol*m*c+c*c+avex*avex)**0.5
        time=zsol-avez
        time/=avevz
        if time>=0:
            g.write("Case #"+str(case)+": "+str(dist)+" "+str(time)+"\n")
        else:
            g.write("Case #"+str(case)+": "+str((avex*avex+avey*avey+avez*avez)**0.5)+" 0\n")
    elif avevy!=0:
        dist=(avex*avex+avez*avez)**0.5
        time=0-avey
        time/=avevy
        if time>=0:
            g.write("Case #"+str(case)+": "+str(dist)+" "+str(time)+"\n")
        else:
            g.write("Case #"+str(case)+": "+str((avex*avex+avey*avey+avez*avez)**0.5)+" 0\n")
    else:
        g.write("Case #"+str(case)+": "+str((avex*avex+avey*avey+avez*avez)**0.5)+" 0\n")
        
g.close()
    
