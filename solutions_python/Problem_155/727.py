t = int(input())
for i in range(t):
    ans = 0
    now = 0
    s = input().split()[1]
    for j in range(len(s)):
        num = int(s[j])
        added = max(0, j - now)
        now += num + added
        ans += added
    print('Case #', i + 1, ': ', ans, sep = '')