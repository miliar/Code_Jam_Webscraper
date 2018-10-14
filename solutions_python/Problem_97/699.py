f=open("input.txt","r")
lists=f.readlines()
tests=int(lists[0])
i=1
while i<=tests:
    values=lists[i].split(' ')        
    int_val=[int(each) for each in values]
    x=int_val[0]
    y=int_val[1]
    length=len(str(y))
    val1=x
    val2=y
    final=0
    mul=10**(length-1)
    if x==y or (y<10):
        final=0
    else:
        while val1<val2:
            cnt=0
            temp=val1
            k=0
            test=[]
            while k<length:                
                temp=(temp/10) + ((temp%10)*mul)
                if temp!=val1 and x<=temp and temp<=y:
                    if temp<val1:
                        cnt=0
                        break
                    elif temp not in test:
                        test.append(temp)
                        cnt+=1
                k=k+1
            if cnt!=0:
                cnt=cnt+1
                final=final+(((cnt)*(cnt-1))/2)
            val1=val1+1
    print "Case #%d: %d" %(i,final)
    i=i+1
