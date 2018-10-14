

n=int(input())

for nb in range(n):
    s=input()
    s=[c for c in s]
    f=0
    for i in range(len(s)-1):
        if s[i]>s[i+1] and not f:
            j=s.index(s[i])
            s[j]=str(int(s[j])-1)
            f=1
    if f:
        for i in range(j+1,len(s)):
            s[i]="9"
    if s[0]=="0":
        s[0]=""
    print("Case #"+str(nb+1)+": "+"".join(s))
