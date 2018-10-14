f=open("B-small-attempt3.in","r")
t=int(f.readline())
f1=open("output.out","w")
i=1
while(i<=t):
    k=int(f.readline())    
    while(True):
        l=[x for x in str(k)]
        if(k==int("".join(sorted(l)))):
            f1.write("Case #{}: {}\n".format(i,k))
            break
        k-=1
    i+=1
f.close()
f1.close()
