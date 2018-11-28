def flip(s,j,k):
    for i in range(j,j+k):
        if s[i]=='-':
            s[i]='+'
        else:
            s[i]='-'

noTests=int(input())
for i in range(1,noTests+1):
    s,k=input().strip().split()
    s=list(s)
    k=int(k)
    length=len(s)
    p=length-k+1
    count=0
    for j in range(length-k+1):
        if s[j]=='-':
            flip(s,j,k)
            count+=1

    flag=True
    for k in range(j+1,length):
        if s[k]=='-':
            flag=False
            break
    if flag:
        string=count
    else:
        string='IMPOSSIBLE'

    print("Case #{}: {}".format(i,string))

