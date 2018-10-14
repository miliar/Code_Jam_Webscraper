def flip(s,pos,k):
    for i in range(k):
        if s[pos+i]=='-':
            s[pos+i]='+'
        else:
            s[pos+i]='-'

t = int(input())
for i in range(t):
    s = input().split(' ')
    k=int(s[1])
    s=list(s[0])
    flips = 0

    pos = 0
    while True:
        while pos<len(s) and s[pos]=='+':
            pos+=1
        if pos + k > len(s):
            break
        flip(s,pos,k)
        flips+=1
    
    if pos >= len(s):
        res = flips
    else:
        res = "IMPOSSIBLE"
    
    print("Case #{}: {}".format(i+1,res))