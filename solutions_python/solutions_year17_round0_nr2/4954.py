def abc(n):
    nexti=n%10
    n=n/10
    while(n):
        dig=n%10
        if(dig>nexti):
            return False
        nexti=dig
        n=n/10
    return True
t=int(raw_input())
for m in range(0,t):
    x=long(raw_input())
    h=str(x)
    while(abc(x)==False):
        x=x-1
    print "Case #"+str(m+1)+": "+str(x)