def solve():
    inp = raw_input()
    s, k = inp.split(" ")[0], int(inp.split(" ")[1])
    sum = 0
    f = [0 for j in range(len(s))]
    ans = 0
    for j in range(len(s) - k + 1):
        if (s[j] == '-' and (1 + sum) % 2 == 1) or (s[j] == '+' and (sum) % 2 == 1):
            f[j] = 1
            ans += 1
        sum += f[j]
        if j - k + 1 >= 0:
            sum -= f[j - k + 1]

    for j in range(len(s) - k + 1, len(s)):
        if (s[j] == '-' and (1 + sum) % 2 == 1) or (s[j] == '+' and (sum) % 2 == 1):
            return "IMPOSSIBLE"
        if j - k + 1 >= 0:
            sum -= f[j - k + 1]
    return ans




T = int(raw_input())
for i in range(T):
    print solve()


