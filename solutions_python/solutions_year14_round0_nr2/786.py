with open("input2.in") as f:
    line=list(f)
    test=int(line[0])
    i=1
    for t in range(1,test+1):
        r=2.0
        s=line[i]
        i+=1
        l=s.split()
        l=map(float,l)
        c=l[0]
        f=l[1]
        x=l[2]
        if x<=c:
            time=x/r
        else:
            time=c/r
            while x/(r+f) < (x-c)/r:
                r+=f
                time+=c/r
            time+=(x-c)/r
        print "Case #"+str(t)+": "+str(time)

    
