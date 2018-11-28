t=int(input())
i=1
while i<=t:
    y=int(input())
    acc=0
    factor=1
    key=9
    while(y>0):
        mod=y%10
        y=y//10
        if(mod==0):
            y-=1
            acc=factor*10-1
            key=9
        elif(mod>key):
            acc=mod*factor-1
            key=mod-1
        else:
            key=mod
            acc+=mod*factor
        factor*=10
    print("Case #"+str(i)+": "+str(acc))
    i+=1
