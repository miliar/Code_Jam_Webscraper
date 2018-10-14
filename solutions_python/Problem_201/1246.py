ff=open("C-large.in",'r')
pp=ff.readlines()
for kk in range(int((pp[0].split("\n"))[0])):
    g=kk+1
    ss=(pp[g].split("\n"))[0].split(" ")
    a,tt=int(ss[0]),int(ss[1])

    t=tt
    
    if tt==1:
        if a%2==0:
            x,y= a/2,(a/2)-1
        else:
            x,y= a/2,a/2
    else:
        v=len(str(bin(t))[2:])
        sm=0
        ii=0
        for i in xrange(v,0,-1):
            sm=2**i
            if sm<=t:
                ii=i-1
                break
        vm=(2**(ii+1))-1
        #print "VM",ii,vm
        par=a/(vm+1)
        rem=a%(vm+1)
        cal=rem+1
        #print str(bin(t))[2:],v,par,rem,cal
        p=t-vm
        #print p
        if p<=cal:
            if par%2==0:
                x,y= par/2,(par/2)-1
            else:
                x,y= par/2,par/2
        else:
            if par%2==0:
                x,y= (par/2)-1,(par/2)-1
            else:
                x,y= par/2,(par/2)-1
    print "Case #"+str(g)+": "+str(x)+" "+str(y)
