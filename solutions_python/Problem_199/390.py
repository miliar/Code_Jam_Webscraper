def solve(test_num):
    s = input().split()
    k = int(s[1])
    s = list(s[0])
    for i in range(len(s)):
        if s[i] == '-':
            s[i] = 0
        else:
            s[i] = 1
    ans = 0
    i = 0
    n = len(s)
    while i + k <= n:
        if s[i] == 0:
            ans += 1
            for j in range(i, i + k):
                s[j] = 1 - s[j]
        i += 1
    if 0 in s:
        ans = "IMPOSSIBLE"
    print("Case #", test_num, ": ", ans, sep="")

for i in range(1, int(input()) + 1):
    solve(i)

