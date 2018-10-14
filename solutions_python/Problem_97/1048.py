def lead():
    fil=open('C-small-attempt0.in','r')
    x=fil.readline()
    i=1
    p = open("rever10.in","w")
    while i<=int(x):
        c=0
        y=fil.readline()
        link=y.split()
        link1=[]
        for e in range(int(link[0]),int(link[1])+1):
            z=str(e)
            rev=''
            for f in range(1,len(z)):
                if(not(z[f]=='0')):
                    rev=z[f:]+z[:f]
                    if int(rev) in range(e,int(link[1])+1) and not(int(rev)==int(z)):
                        if int(rev)>e:
                            l=[e,int(rev)]
                            if l not in link1:
                                link1.append(l)
                                c=c+1
        p.write("Case #"+str(i)+": "+str(c)+"\n")
        i=i+1
    p.close()
    fil.close()

                              
lead()                           
