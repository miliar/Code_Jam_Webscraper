case=int(input())
z=1
while z<=case:
    l=input().split()
    smax=int(l[0])
    string=l[1]
    sump=int(string[0])
    count=0
    for i in range(1,smax+1):
        if string[i]!='0':
            if(i<=sump):
                sump+=int(string[i])
            else:
                count+=(i-sump)
                sump=i+int(string[i])
    print("Case #"+str(z)+":",count)
    z+=1
        
