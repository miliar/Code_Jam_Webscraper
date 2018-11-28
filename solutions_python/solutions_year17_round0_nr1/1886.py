t = int(input())

for _ in range(t):
    s,k = map(str,raw_input().strip().split(" "))
    k = int(k)

    l = len(s)
    x = 0
    for i in range(l):
        if s[i]=='+':
            y = l-1-i
            x = x^(1<<y)

    d = ((1<<l)-1)
    
    level = [-1]*100000
    level[x] = 0
    
    q = []
    q.append(x)
    while(len(q)!=0):
        u = q.pop(0)
        if u==d:
            break
        for i in range(l-k+1):
            m=u
            for j in range(i,i+k):
                m=m^(1<<j)
            if level[m]==-1:
                level[m]=level[u]+1
                q.append(m)

    if level[d]==-1:
        ans = "Case #%d: "%(_+1)+"IMPOSSIBLE"
    else:
        ans = "Case #%d: "%(_+1)+str(level[d])
    print ans
