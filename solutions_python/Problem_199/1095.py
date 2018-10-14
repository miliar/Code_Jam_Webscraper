def solve(_s, k):
    s = list(_s)
    ans = 0
    for i in range(len(s) - k + 1):
        if s[i] == '-':
            ans += 1
            for j in range(i, i + k):
                s[j] = '-' if s[j] == '+' else '+'
    if '-' in s:
        return 'IMPOSSIBLE'
    return ans


T = int(input())
for t in range(1, T + 1):
    S, K = input().split(" ")
    K = int(K)

    ANS = solve(S, K)
    print("Case #{}: {}".format(t, ANS))
