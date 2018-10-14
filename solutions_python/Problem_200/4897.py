def checkTidy(n):
    num=list(str(n))
    return num==sorted(num)

inp=int(raw_input())

for i in range(0,inp):
    n=long(raw_input())
    j=n
    tnum=0
    #print len(str(n))
    while(j>=0):
        if(checkTidy(j)):
            tnum=j
            break
        j-=1
    st="Case #"+str(i+1)+":"
    print st,tnum

        
        
    
