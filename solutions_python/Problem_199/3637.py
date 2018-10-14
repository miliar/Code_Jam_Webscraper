# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    inp = input().strip().split(' ')
    s = list(inp[0])
    k = int(inp[1])
    n = len(s)
    ans = 0
    for idx in range(n - k + 1):
        if s[idx] == '-':
            ans += 1
            for j in range(idx, idx + k):
                if s[j] == '+':
                    s[j] = '-'
                else:
                    s[j] = '+'
    if s == ['+']*n:
        print("Case #{}: {}".format(i, ans))
    else:
        print("Case #{}: IMPOSSIBLE".format(i))
