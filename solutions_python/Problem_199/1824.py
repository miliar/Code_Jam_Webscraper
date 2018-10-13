q=int(input())
temp=q
while q>0:
    q-=1
    s,z=(input().split())
    z=int(z)
    li=list(s)
    change=1
    totadd=0
    while change==1:
        if change==1:
            change=0
            for i in range(len(li)-z+1):
                if li[i]=="-":
                    totadd+=1
                    change=1
                    for j in range(z):
                        if li[i+j]=="-":
                            li[i+j]="+"
                        else:
                            li[i+j]="-"
                    
        else:
            break 
    if li.count("+")==len(li):
        print("Case #{}: {}".format(temp-q,totadd))
    else:
        print("Case #{}: IMPOSSIBLE".format(temp-q))
