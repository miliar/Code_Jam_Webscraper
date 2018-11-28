def solve():
    s,k = input().split()
    k=int(k)
    s=[c for c in s]
    c=0
    for i in range(len(s)-k+1):
        if s[i]=='-':
            c+=1
            for j in range(i,i+k):
                if s[j]=='-':
                    s[j]='+'
                else:
                    s[j]='-'

    if '-' in s:
        return "IMPOSSIBLE"
    return str(c)


T=int(input())
for t in range(1,T+1):
    print("Case #%d: %s" % (t, solve()))
