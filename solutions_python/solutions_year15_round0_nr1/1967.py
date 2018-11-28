def solve():
    smax, s = input().split()
    smax = int(smax)
    s = [int(c) for c in s]
    cur = 0
    a = 0
    for i in range(smax+1):
        if cur < i and s[i] > 0:
            a += i - cur
            cur = i
        cur += s[i]
    return a
T = int(input())
for t in range(T):
    print("Case #%d: %s" % (t+1, solve()))
