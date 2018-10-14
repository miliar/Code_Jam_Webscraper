T = input()

for t in  range(T):
    s,k = raw_input().split(" ")
    s = int(s)
    
    ans = 0
    cnt = 0
    ans = 0
    for i in range(s+1):
        if (ans + cnt) < i:
            ans += i - (cnt + ans)
        cnt += int(k[i])
    print "Case #%d: %d"%(t+1,ans)
    