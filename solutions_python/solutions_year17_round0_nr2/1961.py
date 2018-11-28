q=int(input())
k=0
lm=0
z=q
while q>0:
    q-=1
    x=int(input())
    while x>0:
        s=list(str(x))
        s=[int(x) for x in s]
        x-=1
        flag=0
        for j in range(1,len(s)):
            if s[j-1]<=s[j]:
                continue
            else:
                flag=1
                s[j-1]-=1
                lm=s[j]
                for lmn in range(j,len(s)):
                    s[lmn]=9
        s=[str(x) for x in s]
        x=int(''.join(s))
        if flag==1:
            continue
        else:
            print("Case #{}: {}".format(z-q,x))
            break