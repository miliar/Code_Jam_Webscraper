q=int(input())
z=q
while q>0:
    q-=1
    x=int(input())
    while x>0:
        s=list(str(x))
        x-=1
        flag=0
        for j in range(1,len(s)):
            if s[j-1]<=s[j]:
                continue
            else:
                flag=1
        if flag==1:
            continue
        else:
            print("Case #{}: {}".format(z-q,x+1))
            break
