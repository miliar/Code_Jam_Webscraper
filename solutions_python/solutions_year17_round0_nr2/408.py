def solve(test_num):
    s = list(map(int, list(input())))
    for i in range(1, len(s)):
        if s[i - 1] > s[i]:
            j = i - 1
            while j > 0 and s[j] == s[j - 1]:
                j -= 1
            s[j] -= 1
            j += 1
            while j < len(s):
                s[j] = 9
                j += 1
            break
    if s[0] == 0:
        s.pop(0)
    ans = "".join(str(x) for x in s)
    print("Case #", test_num, ": ", ans, sep="")

for i in range(1, int(input()) + 1):
    solve(i)

