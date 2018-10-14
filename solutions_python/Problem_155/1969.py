for _ in range(input()):
    c1,s1=map(str,raw_input().split())
    l=str(s1)
    a=[]
    #print int(l[0])
    a=map(int,l)
    #print a
    count=0
    c=int(c1)
    temp=0
    for i in range(c+1):
        t=0
        temp=temp+a[i]
        t=(i+1)
        #print i,temp,t
        if(temp>=t):
            continue
        else:
            temp=temp+1
            count=count+1
    print "Case #"+str(_+1)+": "+str(count)
