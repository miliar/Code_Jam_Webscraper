def pan(s,k):
    for i in range(len(s)):
        if s[i] == '+':
            s[i] = 1
        else:
            s[i] = -1
    op = 0
    for j in range(len(s) - k + 1):
        if s[j] == -1:
            s[j:j + k] = [-1*e for e in s[j:j + k]]
            op += 1
    if s[-k:] == [1 for i in range(k)]:
        return op
    else:
        return "IMPOSSIBLE"

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    s = input().split()
    k = int(s.pop(-1))
    s = list(s[0])
    res = pan(s,k)
    print("Case #{}: {}".format(i, res))
