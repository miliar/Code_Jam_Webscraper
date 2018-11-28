t = int(input())
for i in range(t):
    d = int(input())
    p = list(map(int, input().split()))
    ans = max(p)
    for s in range(1, max(p)):
        d = 0
        for now in p:
            d += (now - 1) // s
        ans = min(s + d, ans)
    print('Case #', i + 1, ': ', ans, sep = '')
    
        