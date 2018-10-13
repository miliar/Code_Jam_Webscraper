q=int(input())
temp=q
while q>0:
    q-=1
    s,k=(input().split())
    k=int(k)
    l=list(s)
    change=1
    coun=0
    while change==1:
        if change==1:
            change=0
            for i in range(len(l)-k+1):
                if l[i]=="-":
                    coun+=1
                    change=1
                    for j in range(k):
                        if l[i+j]=="-":
                            l[i+j]="+"
                        else:
                            l[i+j]="-"
                    
        else:
            break 
    if l.count("+")==len(l):
        print("Case #{}: {}".format(temp-q,coun))
    else:
        print("Case #{}: IMPOSSIBLE".format(temp-q))
