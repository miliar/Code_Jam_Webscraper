n=int(raw_input())
for i in range(0,n):
    c,f,x=map(float,raw_input().split(" "))
    #print c,f,x,"\n"
    l=[x/2.0,x/2.0,x/2.0,x/2.0,]
    sig1=0
    j=0
    time=0
    while 1:
        #print l
        sig1+=c/(2.0+j*f)
        sig2=x/(2.0+(j+1)*f)
        #print sig1,sig2
        l.append(sig1+sig2)
        j+=1
        if(j==4):
            tmp=min(l)
            if(l.index(tmp)<3):
                print "Case #"+str(i+1)+": "+"%.7f"%(tmp)
                break
        else:
            if(l[0]>l[1] and l[1]<l[2]):
            #if(l[0]>l[1]):
                print "Case #"+str(i+1)+": "+"%.7f"%(l[1])
                break
        if(len(l)>4):
            l.pop(0)

print ""
        
