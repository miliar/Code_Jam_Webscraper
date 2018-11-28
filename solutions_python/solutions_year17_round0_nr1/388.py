def solve(s, k):
    s = list(s)
    k = int(k)
    ans = 0
    while s:
        if s.pop() != '+':
            if len(s) < k - 1: return "IMPOSSIBLE"
            for i in range(1, k):
                s[-i] = '-' if s[-i] == '+' else '+'
            ans += 1
    return ans

for i in range(1, int(input()) + 1):
    print("Case #", i, ": ", solve(*input().split()), sep='')
