fi = open("A-large.in", "r")
fo = open("A.out", "w")
T = int(fi.readline().rstrip())
for t in range(1, T + 1):
    s, k = fi.readline().rstrip().split()
    k = int(k)
    n = len(s)
    dp = [0 for q in range(n + k - 1)]
    tmp = 0
    good = True
    for i in range(n - k + 1):
        if s[i] == '+':
            dp[i] = (0 if tmp % 2 == 0 else 1)
        else:
            dp[i] = (1 if tmp % 2 == 0 else 0)
        tmp += dp[i] - dp[i - k + 1]
    for i in range(n - k + 1, n):
        if (s[i] == '+' and tmp % 2 == 1) or (s[i] == '-' and tmp % 2 == 0):
            good = False
            break
        tmp += dp[i] - dp[i - k + 1]
    if not good:
        fo.write("Case #%d: IMPOSSIBLE\n" % t)
    else:
        fo.write("Case #%d: %d\n" % (t, sum(dp)))