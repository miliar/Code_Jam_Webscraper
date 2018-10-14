def tidy(n):
    if n<10:
        return(n)
    s=list(str(n))
    a=set(s)
    l=len(s)
    if a=={'0','1'}:
        ans='9'*(l-1)
        return(int(ans))
    p=-1
    ans=s
    while(True):
        if (ans==''.join(sorted(list(ans)))):
            break
        for i in range(l-1):
            if s[i+1]<s[i]:
                p=i+1
                s[i]=str(int(s[i])-1)
                break
        if p!=-1:
            ans=''.join(s[:p])+'9'*(l-p)
    return(ans)
    
n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
for i in range(n):
    print("Case #"+str(i+1)+": "+str(tidy(l[i])))
