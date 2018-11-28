def solve(case_no):
    s, k = input().split()
    s = list(s)
    k = int(k)

    ans = 0
    for i in range(len(s) - k + 1):
        if s[i] == '-':
            for j in range(k):
                s[i+j] = '-' if s[i+j] == '+' else '+'
            ans += 1

    print('Case #{}:'.format(case_no), end=' ')
    if not s.count('-'):
        print(ans)
    else:
        print("IMPOSSIBLE")

t = int(input())
for i in range(t):
    solve(i + 1)
