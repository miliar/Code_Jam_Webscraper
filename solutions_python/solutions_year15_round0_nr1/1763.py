T = int(input())
for t in range(1,T+1):
    c, s = input().split()
    ans = 0
    k = 0
    for i in range(len(s)):
        c = int(s[i])
        if c > 0 and k < i:
            ans += i - k
            k += i - k
        k += c
        
    print('Case #'+str(t)+':', ans)
        