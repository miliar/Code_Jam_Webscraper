for x in range(int(input())):
    n, s = input().split()
    ans, cur = 0, 0
    for i in range(int(n) + 1):
        if i > cur:
            ans += i - cur
            cur = i + int(s[i])
        else:
            cur += int(s[i])
#        print(cur, ans)
    print("Case #", x + 1, ": ", ans, sep = "")

