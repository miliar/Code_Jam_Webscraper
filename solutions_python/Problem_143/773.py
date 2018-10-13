t=int(input())
case=0;
while t>0 :
    t-=1;case+=1;
    [a,b,k]=map(int,raw_input().split())
    cnt=0;
    i=0;
    while i<a:
        j=0;
        while j<b:
            if (i&j)<k:
                cnt+=1
                #print (i,j),
            j+=1
        i+=1
    print "Case #"+str(case)+": "+str(cnt)
    
