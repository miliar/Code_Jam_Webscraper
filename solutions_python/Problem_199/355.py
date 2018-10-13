t = int(raw_input())

for i in range(1,t+1):

    s,k = raw_input().strip().split(' ')
    s = list(s)
    k = int(k)
    f = 1
    ans = 0
    
    for j in range(len(s)-k+1):
        if(s[j]=='+'): continue
        for p in range(j,j+k): s[p] = '+' if s[p]=='-' else '-'
        ans+=1

    for j in range(len(s)):
        if(s[j]=='-'):
            f=0
            break

    if(f): print "Case #%d: %d" %(i,ans)
    else: print "Case #%d: IMPOSSIBLE" %(i)
