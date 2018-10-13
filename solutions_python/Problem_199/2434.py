def run(test):
    s, k = input().split()
    s = list(s)
    k = int(k)
    ans = 0
    for i in range(len(s) - k + 1):
        if s[i] == '-':
            ans += 1
            for j in range(k):
                s[i + j] = {
                    '-' : '+',
                    '+' : '-'
                }[s[i + j]]
    if s != ['+'] * len(s):
        ans = "IMPOSSIBLE"
    print("Case #{}: {}".format(test, ans))

t = int(input())

for i in range(t):
    run(i + 1)