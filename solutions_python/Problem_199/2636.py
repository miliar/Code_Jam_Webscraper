def solve(s, k):
    ans = 0
    n = len(s)
    ov = [0 for _ in range(n)]
    for i in range(n-k+1):
        if s[i] == '+' and ov[i] % 2 == 1 or s[i] == '-' and ov[i] % 2 == 0:
            for j in range(i, i+k):
                ov[j] += 1
            ans += 1
    while i < n:
        if s[i] == '+' and ov[i] % 2 == 1 or s[i] == '-' and ov[i] % 2 == 0:
            return "IMPOSSIBLE"
        i += 1
    return str(ans)

t = int(input())
for i in range(t):
    s, k = input().split()
    k = int(k)
    print("Case #%d: %s"%(i+1, solve(s, k)))



