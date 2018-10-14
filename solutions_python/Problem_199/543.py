
def solve():
    s, k = input().split()
    k = int(k)
    f = [0] * (1 + len(s))
    alc = 0
    ans = 0
    for i in range(len(s)):
        alc ^= f[i]
        if (s[i] == '+') == alc:
            if i + k > len(s):
                ans = -1
                break
            else:
                alc ^= 1
                f[i + k] = 1
                ans += 1

    print("IMPOSSIBLE" if ans == -1 else ans)

T = int(input())
for t in range(T):
    print("Case #%d: " % (t + 1), end = '')
    solve()
