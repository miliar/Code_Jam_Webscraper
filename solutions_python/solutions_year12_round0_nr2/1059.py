def google():
    fil=open('B-large.in','r')
    x=fil.readline()
    i=1
    p = open("rever4.in","w")
    while i<=int(x):
        c=0
        y=fil.readline()
        link=[]
        lin=y.split()
        for e in lin:
            link.append(int(e))
        link1=link[3:]
        s=link[1]
        
        if len(link1)==link[0]:
            for e in link1:
                sup=[]
                unsup=[]
        
                if e%3==0:
                    if e==0 or e==30:
                        sup=[e/3,e/3,e/3]
                    else:
                        sup=[e/3,e/3,e/3]
                        unsup=[e/3-1,e/3,e/3+1]
                elif e%3==1:
                    if e==1:
                        sup=[e/3+1,e/3,e/3]
                    else:
                        sup=[e/3+1,e/3,e/3]
                        unsup=[e/3+1,e/3+1,e/3-1]
                else:
                    if e==29:
                        sup=[e/3+1,e/3+1,e/3]
                    else:
                        sup=[e/3+1,e/3+1,e/3]
                        unsup=[e/3+2,e/3,e/3]
                flag=1
                for e in sup:
                    if e>=link[2]:
                        c=c+1
                        flag=0
                        break
                if flag and s and unsup:
                    for e in unsup:
                        if e>=link[2]:
                            s=s-1
                            c=c+1
                            break
        p.write("Case #"+str(i)+": "+str(c)+"\n")
        i=i+1
    p.close()
    fil.close()


google()
            
