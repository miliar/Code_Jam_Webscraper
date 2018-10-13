def f(n):
    if n<10:
        return(n)
    
    s=list(str(n))
    a=set(s)
    l=len(s)
    if a=={'0','1'}:
        ans='9'*(l-1)
        return(int(ans))
    pos=-1
    for i in range(l-1):
        if s[i+1]<s[i]:
            pos=i+1
            s[i]=str(int(s[i])-1)
            break
    if pos!=-1:
        answer=''.join(s[:pos])+'9'*(l-pos)
        return(str(int(answer)))
    else:
        return(n)

a=[]
n=int(input())
for i in range(n):
    a.append(int(input().strip()))

for i in range(n):
    print("Case #{}: {}".format(i+1, f(a[i])))
    
