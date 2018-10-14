import sys

sys.setrecursionlimit(10000)

n = int(input())
def g(s):
    ns = ''.join(['+' if c == '-' else '-' for c in s])
    return ns
def f(s, k, c):
    i = s.find('-')
    if i == -1:
        return c
    if len(s) - i + 1 <= k:
        return -1
    s = s[:i] + g(s[i:i+k]) + s[i+k:]
    r = f(s, k, c+1)
    return r if r != -1 else -1

for i in range(n):
    s, k = input().split()
    k = int(k)
    r = f(s, k, 0)
    print("Case #" + str(i+1) + ": " + (str(r) if r > -1 else "IMPOSSIBLE"))
