from sys import stdin

def solve(t):
    chars = list(stdin.readline().strip())
    s = list(map(int, chars))
    last = int(s[len(s) - 1])
    for i in range(len(s) - 2, -1, -1):
        current = s[i]
        if current > last:
            s[i] -= 1
            for j in range(i + 1, len(s)):
                s[j] = 9
        last = s[i]

    res = 0
    for d in s:
        res = res * 10 + d
    print('Case #' + str(t + 1) + ': ' + str(res))

T = int(stdin.readline())
for t in range(0, T):
    solve(t)
