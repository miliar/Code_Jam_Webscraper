def gcd(x,y):
    if(x<y):
        return gcd(y,x)
    if((x%y)==0):
        return y
    return gcd(y,x%y)

a = raw_input()
test=int(a)
for i in range(0,test):
    a = raw_input()
    lis = a.split(" ")
    ans=-1
    for j in range(1,len(lis)):
        for k in range(j+1,len(lis)):
            if(lis[j]==lis[k]):
                continue
            if(ans==-1):
                ans=abs(int(lis[j])-int(lis[k]))
            else:
                ans=gcd(ans,abs(int(lis[j])-int(lis[k])))
    y=int(lis[1])%ans
    y=ans - y
    y=y%ans
    print "Case #" + str(i+1) + ": " + str(y)

        
