t=int(input())
for i in range(t):
    n=list(input())
    for j in range(len(n)-1,0,-1):
        if(int(n[j])<int(n[j-1])):
            n[j-1]=str(int(n[j-1])-1)
            for k in range(j,len(n)):
                n[k]='9'
    print("Case #{}: {}".format(i+1,int(''.join(n))))
    
